#!/usr/bin/python3
# city.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class named City; implementation."""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that inherits from BaseModel and represent
    a City
    """
    state_id = "State.id"
    name = ""
