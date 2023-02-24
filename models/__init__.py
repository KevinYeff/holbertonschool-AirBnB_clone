#!/usr/bin/python3
"""This module creates a unique FileStorage instances and reloads the objects.
"""


from models.engine.file_storage import file_storage


storage = FileStorage()
storage.reload()
