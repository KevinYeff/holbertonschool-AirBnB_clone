#!/usr/bin/python3
# file_storage.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class FileStorage that serializes instances.
"""

import json
import os
import models


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
        self.__objects[k_obj] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path).
        """
        f_in = self.__file_path
        d = {}
        for k, v in self.__objects.items():
            d[k] = v.to_dict()
        with open(f_in, "w", encoding="utf-8") as f_out:
            json.dump(d, f_out)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        f_in = self.__file_path
        if os.path.exists(f_in):
            with open(f_in, "r", encoding="utf-8") as f_out:
                obj_dict = json.load(f_out)
                objs_loaded = {}
                for k, v in obj_dict.items():
                    cls = v["__class__"]
                    obj_class = models.models_classes[cls]
                    obj_instance = obj_class(**v)
                    objs_loaded["{}.{}".format(cls, k)] = obj_instance
                self.__objects.update(objs_loaded)
