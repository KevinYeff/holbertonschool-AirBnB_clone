#!/usr/bin/python3
"""This module creates a unique FileStorage instances and reloads the objects.
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


models_classes = {
    "BaseModel": BaseModel,
    "User": User
}

storage = FileStorage()
storage.reload()
