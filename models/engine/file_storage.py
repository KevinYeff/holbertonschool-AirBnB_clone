#!/usr/bin/python3
# file_storage.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class FileStorage that serializes instances.
"""

import json
import os


class FileStorage:
    """Represent a file storage of instances.
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Return the dictionary of the class attribute(__objects).
        """
        return(FileStorage.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key (<obj class name>.id).
        """
        k_obj = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k_obj] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path).
        """
        f_in = FileStorage.__file_path
        d = FileStorage.__objects          
        with open("f_in", "w", encoding="utf-8") as f_out:
            json.dump(d, f_out)

    def reload(self):
        """Deserializes the JSON file to __objects.
        """
        f_in = FileStorage.__file_path
        d = FileStorage.__objects
        if os.path.exists(f_in):
            with open("f_in", "r", encoding="utf-8") as f_out:
                d = json.load(f_out)
