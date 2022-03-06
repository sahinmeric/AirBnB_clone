#!/usr/bin/python3
"""
Test module for file_storage
"""


import os
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """ Test cases for File storage"""

    def test_doc(self):
        """ test for documentation"""
        fs = FileStorage()
        self.assertNotEqual(len(fs.__doc__), 0)
        self.assertNotEqual(len(fs.all.__doc__), 0)
        self.assertNotEqual(len(fs.new.__doc__), 0)
        self.assertNotEqual(len(fs.save.__doc__), 0)
        self.assertNotEqual(len(fs.reload.__doc__), 0)

    def test_type(self):
        """ test the type of the instance"""
        fs = FileStorage()
        self.assertEqual(str(type(fs)),
                         "<class 'models.engine.file_storage.FileStorage'>")

    def test_permissions(self):
        """ checks the permissions"""
        rd = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(rd, "Read permission is False")
        wr = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(wr, "Write permission is False")
        ex = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertFalse(ex, "Execute permission is True")

    if __name__ == '__main__':
        unittest.main()
