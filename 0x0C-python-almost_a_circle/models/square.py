#!/usr/bin/python3
"""This module contains the Square class, inheriting from the Rectangle class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instances."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str special method."""
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_square + str_id + str_xy + str_size

    @property
    def size(self):
        """Getter size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method."""
        if args and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if list_atr[i] == 'size':
                    setattr(self, 'width', arg)
                    setattr(self, 'height', arg)
                else:
                    setattr(self, list_atr[i], arg)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary with attributes."""
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
