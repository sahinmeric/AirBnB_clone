#!/usr/bin/python3
"""
Unittest for base_model
"""
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def checkdocst(self):
        """check docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def testfrm(self):
        """check str format"""
        bm = BaseModel()
        self.assertEqual(str(bm), f'[BaseModel] ({bm.id} \
                {bm.__dict__}')
        # datetime
        self.assertEqual(type(bm.created_at), datetime)
        self.assertEqual(type(bm.updated_at), datetime)
        # int
        bm.num1 = 89
        self.assertTrue(hasattr(bm, "num1"))
        self.assertEqual(type(bm.num1), int)
        # str for name
        bm.nam1 = "Testing"
        self.assertTrue(hasattr(bm, "nam1"))
        self.assertEqual(type(bm.nam1), str)
