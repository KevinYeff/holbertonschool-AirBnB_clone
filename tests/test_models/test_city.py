#!/usr/bin/python3
# test_city.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define Test for class City."""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test suites for class State."""

    def test_doc_module(self):
        """Test module documentation."""
        actual = models.city.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = City.__doc__
        self.assertIsNotNone(actual)

    def test_attributes(self):
        """Test attributes for the city object."""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_attributes_type(self):
        """Test that object attributes are the same type."""
        self.assertTrue(type(self.city.name) == str)
        self.assertTrue(type(self.city.state_id) == str)
      
if __name__ == '__main__':
    unittest.main
