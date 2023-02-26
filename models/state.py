#!/usr/bin/python3
# state.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define a class named state; implementation."""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class that inherits from BaseModel and represent
    a state.
    """
    name = ""
