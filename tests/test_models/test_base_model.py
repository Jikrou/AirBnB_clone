#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Unittest testing for the BaseModel class"""
    def test_uuid(self):
        """Test if uuid is a string and also unique"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1.id, str)
        self.assertTrue(hasattr(bm2, "id"))
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_and_updated_at(self):
        """Test the created_at is assigned the current time
            and updated_at is assigned the current time when save() is called
        """
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
        #test if update_at datetime updates after save method is called
        previous = bm1.updated_at
        bm1.save()
        current = bm1.updated_at
        self.assertNotEqual(previous, current)

    def test_to_dict(self):
        """Test if the to_dict method returns a dictionary"""
        bm1 = BaseModel()
        bm1.name = "model_test"
        bm1.numbers = 11
        bm1.save()
        bm1_dict = bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertEqual(bm1_dict["name"], "model_test")
        self.assertEqual(bm1_dict["numbers"], 11)
        bm2 = BaseModel()
        bm2_dict = bm2.to_dict()
        self.assertIsInstance(bm2_dict, dict)
        self.assertIsInstance(bm2_dict["created_at"], str)
