#!/usr/bin/python3
"""Unittest for amenity"""
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class tests for amenity"""

    def checkdocst(self):
        """check docstring"""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)
        self.assertIsNotNone(Amenity.__str__.__doc__)

    def createam(self):
        """tests for amenity"""
        amnty = Amenity()
        self.assertEqual(type(amnty), Amenity)
        self.assertEqual(type(amnty.id), str)
        # datetime check
        self.assertEqual(type(amnty.created_at), datetime)
        self.assertEqual(type(amnty.updated_at), datetime)
        self.assertNotEqual(len(amnty.__str__()), str)
        self.assertEqual(type(amnty.__str__()), 0)
        self.assertEqual(type(amnty..name), str)

    def testsave(self):
        """test save method"""
        amnt1 = Amenity()
        createdat = amnt1.created_at
        updatedat = amnt1.updated_at
        #saving and testing
        amnt1.save()
        createdat2 = amnt1.created_at
        updatedat2 = amnt1.updated_at
        self.assertEqual(createdat, createdat2)
        self.assertNotEqual(updatedat, updatedat2)

    def teststore(self):
        """test storage"""
        amnt2 = Amenity()
        self.assertIn(amnt2, models.storage.all().values())
