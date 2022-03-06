#!/usr/bin/python3
"""
Unittest for city_model
"""
import models
import unittest
from models.base_model import BaseModel
from models.city_model import City


class TestCity(unittest.TestCase):
    """testing city"""

    def checkdocst(self):
        """check docstring"""
        self.assertIsNotNone(City.__doc__)

    def testcity(self):
        """check class and attrs"""
        cty = City()
        self.assertIsInstance(cty, City)
        self.assertIsInstance(cty, BaseModel)
        self.assertTrue(hasattr(cty, "state_id"))
        self.assertIsInstance(cty.state_id, str)
        self.assertTrue(hasattr(cty, "name"))
        self.assertIsInstance(cty.name, str)

        #check str
        self.assertEqual(str(cty), f'[City] ({cty.id} \
                {cty.__dict__}')

    def testmthds(self):
        """test methods"""
        ct1 = City()
        self.assertEqual(type(ct1.to_dict()), dict)
