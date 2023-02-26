#!/usr/bin/python3
# test_base_model.py
# Alex Nuñez <5694@holbertonstudents.com>
# Yeff Espinoza <5153@holbertonstudents.com>
"""Test for class BaseModel."""


import unittest
from models.base_model import BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Class for testing BaseModel docs."""

    def setUp(self):
        """
        Setup resources to be used in the tests
        i) Create a BaseModel object
        """
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up resources after the tests
        i) Delete the instance created
        """
        del self.base_model

    def test_doc_module(self):
        """Test module documentation."""
        actual = models.base_model.__doc__
        self.assertIsNotNone(actual)

    def test_doc_class(self):
        """Test class documentation."""
        actual = models.base_model.BaseModel.__doc__
        self.assertIsNotNone(actual)

    def test_doc_save(self):
        """Test method save documentation."""
        actual = models.base_model.BaseModel.save.__doc__
        self.assertIsNotNone(actual)

    def test_doc_to_dict(self):
        """Test method to_dict documentation."""
        actual = models.base_model.BaseModel.to_dict.__doc__
        self.assertIsNotNone(actual)

    def test_to_dict(self):
        """Test return to_dict."""
        expect = self.BaseModel.to_dict()
        self.assertIs(type(expect), dict)

    def test_doc__init__(self):
        """Test method __init__ documentation."""
        actual = models.base_model.BaseModel.__init__.__doc__
        self.assertIsNotNone(actual)

    def test_id_value(self):
        """Test value type."""
        expect = models.base_model.BaseModel.self.id
        self.assertIs(type(expect), str)

if __name__ == '__main__':
    unittest.main
