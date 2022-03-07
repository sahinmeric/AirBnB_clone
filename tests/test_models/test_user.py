#!/usr/bin/python3
"""Unittest for user"""
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """class tests for user"""

    def checkdocst(self):
        """check docstring"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)

    def createuser(self):
        """tests for user"""
        userr = User()
        self.assertEqual(type(userr), User)
        self.assertEqual(type(userr.id), str)
        # datetime check
        self.assertEqual(type(userr.created_at), datetime)
        self.assertEqual(type(userr.updated_at), datetime)
        self.assertEqual(type(userr.first_name), str)
        self.assertEqual(type(userr.last_name), str)
        self.assertEqual(type(userr.email), str)
        self.assertEqual(type(userr.password), str)
        # check str
        self.assertEqual(type(userr.__str__()), str)
        self.assertNotEqual(len(userr.__str__()), 0)

    def testsave(self):
        """test save method"""
        user1 = User()
        createdat = user1.created_at
        updatedat = user1.updated_at
        #saving and testing
        user1.save()
        createdat2 = user1.created_at
        updatedat2 = user1.updated_at
        self.assertEqual(createdat, createdat2)
        self.assertNotEqual(updatedat, updatedat2)
