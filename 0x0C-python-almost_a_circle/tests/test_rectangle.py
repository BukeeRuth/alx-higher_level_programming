#!/usr/bin/python3
"""Module for testing the Rectangle class"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """Suite to test the Rectangle class"""

    def setUp(self):
        """Method invoked for each test"""
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """Test new rectangle"""
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_2(self):
        """Test new rectangle with all attrs"""
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """Test new rectangles"""
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """Test Rectangle is a Base instance"""
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """Test error raise with 1 arg passed"""
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    # (Other tests remain unchanged)

    def test_load_from_file(self):
        """Test load JSON file"""
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """Test load JSON file"""
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())


if __name__ == "__main__":
    unittest.main()

