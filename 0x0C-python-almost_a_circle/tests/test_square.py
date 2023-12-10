#!/usr/bin/python3
""" Module for testing the Square class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """ Suite to test the Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Test creating a new square """
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """ Test creating a new square with all attributes """
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """ Test creating new squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertFalse(new is new2)
        self.assertFalse(new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test if Square is a Base instance """
        new = Square(1)
        self.assertTrue(isinstance(new, Base))

    def test_is_Rectangle_instance(self):
        """ Test if Square is a Rectangle instance """
        new = Square(1)
        self.assertTrue(isinstance(new, Square))

    def test_incorrect_amount_attrs(self):
        """ Test error raised with no arguments passed """
        with self.assertRaises(TypeError):
            new = Square()

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with too many arguments passed """
        with self.assertRaises(TypeError):
            new = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        """ Try to access a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    # ... (rest of the test cases remain unchanged)

