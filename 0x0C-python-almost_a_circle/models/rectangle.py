#!/usr/bin/python3
"""This module contains the Rectangle class,
inheriting from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        self.validate_positive_int("width", value)
        self.__width = value

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        self.validate_positive_int("height", value)
        self.__height = value

    @property
    def x(self):
        """ X getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter """
        self.validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """ Y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter """
        self.validate_non_negative_int("y", value)
        self.__y = value

    def validate_positive_int(self, attribute, value):
        """ Validate positive integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def validate_non_negative_int(self, attribute, value):
        """ Validate non-negative integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """ Returns the area of the rectangle object """
        return self.width * self.height

    def display(self):
        """ Displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ Str special method """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return "{}{}{}{}".format(str_rectangle, str_id, str_xy, str_wh)

    def update(self, *args, **kwargs):
        """ Update method """
        if args:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Method that returns a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        return {key: getattr(self, key) for key in list_atr}

