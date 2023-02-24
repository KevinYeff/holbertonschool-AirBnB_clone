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
        self.reload()
        return (self.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key (<obj class name>.id).
        """
        k_obj = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[k_obj] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path).
        """
        f_in = self.__file_path
        d = self.__objects
        with open(f_in, "w", encoding="utf-8") as f_out:
            json.dump(d, f_out)

   def reload(self):
        """Deserializes the JSON file to __objects.
        """
        f_in = self.__file_path
        if os.path.exists(f_in):
            with open(f_in, "r", encoding="utf-8") as f_out:
                obj_dict = json.load(f_out)
                for value in obj_dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
