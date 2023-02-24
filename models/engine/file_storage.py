#!/usr/bin/python3
# file_storage.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class FileStorage that serializes instances.
"""


import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
