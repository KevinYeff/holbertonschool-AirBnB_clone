#!/usr/bin/python3
# amenity.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class named amenity; implementation."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class that inherits from BaseModel and represents
    a behavior
    """
    name = ""
