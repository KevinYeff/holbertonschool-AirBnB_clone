#!/usr/bin/python3
# user.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class user implementation that
inherits from BaseModel class."""


from models.base_model import BaseModel


class User(BaseModel):
    """ Implementing the class User and its attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
