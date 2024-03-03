#!/usr/bin/python3
"""
Test differents behaviors
of the Base class
"""


import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    A class to test the Base Class
    """

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """

        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def setUp(self):
        """
        Setup method to create an instance of BaseModel before each test.
        """

        self.base_model = BaseModel()

    def test_id_is_string(self):
        """
        Test whether the id attribute of BaseModel is a string.
        """

        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test whether the created_at attribute of BaseModel is a datetime object.
        """

        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test whether the updated_at attribute of BaseModel is a datetime object.
        """

        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test whether calling the save method updates the updated_at attribute.
        """

        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict_contains_class_name(self):
        """
        Test whether the dictionary returned by to_dict contains the __class__ key with the class name.
        """

        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at_and_updated_at(self):
        """
        Test whether the dictionary returned by to_dict contains the created_at and updated_at keys.
        """

        obj_dict = self.base_model.to_dict()
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_created_at_updated_at_format(self):
        """
        Test whether the datetime strings in the dictionary returned by to_dict match the ISO format.
        """

        obj_dict = self.base_model.to_dict()
        created_at_str = obj_dict['created_at']
        updated_at_str = obj_dict['updated_at']
        self.assertEqual(datetime.fromisoformat(created_at_str), self.base_model.created_at)
        self.assertEqual(datetime.fromisoformat(updated_at_str), self.base_model.updated_at)
