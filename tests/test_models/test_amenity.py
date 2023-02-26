#!/usr/bin/python3
# test_amenity.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define Test for class Amenity."""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suites for class Amenity."""

    def test_doc_module(self):
        """Test module documentation."""
        actual = models.amenity.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = Amenity.__doc__
        self.assertIsNotNone(actual)

    def test_attributes(self):
        """Test attributes for the amenity object."""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attributes_type(self):
        """Test that object attributes are the same type."""
        self.assertTrue(type(self.amenity.name) == str)
      
if __name__ == '__main__':
    unittest.main
