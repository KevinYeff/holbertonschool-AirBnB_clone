#!/usr/bin/python3
# test_review.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Define Test for class Review."""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test suites for class Review."""

    def test_doc_module(self):
        """Test module documentation."""
        actual = models.review.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = Review.__doc__
        self.assertIsNotNone(actual)

    def test_attributes(self):
        """Test attributes for the review object."""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_attributes_type(self):
        """Test that object attributes are the same type."""
        self.assertTrue(type(self.review.place_id) == str)
        self.assertTrue(type(self.review.user_id) == str)
        self.assertTrue(type(self.review.text) == str)
      
if __name__ == '__main__':
    unittest.main
