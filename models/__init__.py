#!/usr/bin/python3
"""This module creates a unique FileStorage instances and reloads the objects.
"""


from .engine.file_storage import FileStorage
from .base_model import BaseModel


models_classes = {
    "BaseModel": BaseModel
}

storage = FileStorage()
storage.reload()
