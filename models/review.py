#!/usr/bin/python3
# review.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class named Review; implementation."""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that inherits from BaseModel and represent
    a review
    """
    place_id = "Place.id"
    user_id = "User.id"
    text = ""
