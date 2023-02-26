#!/usr/bin/python3
# place.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class named Place; implementation."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class that inherits from BaseModel and represents
    a place
    """
    city_id = "City.id"
    user_id = "User.id"
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
