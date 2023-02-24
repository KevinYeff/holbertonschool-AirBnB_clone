#!/usr/bin/python3
# test_file_storage.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Test for class FileStorage."""


import unittest
import models.engine


class TestFileStorage(unittest.TestCase):
    """Class for testing FileStorage docs."""

    def test_doc_module(self):
        """Test moduel documentation."""
        actual = models.engine.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test for class documentation."""
        actual = models.engine.FileStorage.__doc__
        self.assertIsNotNone(actual)

    def test__file_path(self):
        """Test for class private attribute __file_path."""
        actual = models.engine.FileStorage.__file_path
        self.assertIsNone(actual)
