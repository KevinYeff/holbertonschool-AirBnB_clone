#!/usr/bin/python3
# test_user.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define Test for class User."""


import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """Test suites for class User."""

    def test_doc_module(self):
        """Test module documentation."""
        actual = models.user.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = User.__doc__
        self.assertIsNotNone(actual)

    def test_attributes(self):
        """Test attributes for the user object."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes(self):
        """Test that object attributes are the same type."""
        self.assertTrue(type(self.user.email) == str)
        self.assertTrue(type(self.user.password) == str)
        self.assertTrue(type(self.user.first_name) == str)
        self.assertTrue(type(self.user.last_name) == str)
      
if __name__ == '__main__':
    unittest.main
