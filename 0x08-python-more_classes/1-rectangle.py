#!/usr/bin/python3
"""
    a simple python module about a rectangle class
"""


class Rectangle:
    """
        Attributes:
            
    """
    def __init__(self, width=0, height=0):
        self._Rectangle__height = height
        self._Rectangle__width = width

        if (width < 0):
            ValueError("raise width must be >= 0")
        if type(self._Rectangle__width) is not int:
            raise TypeError("height must be an integer")
        if (self._Rectangle__height < 0):
            raise ValueError("height must be >= 0")
        if type(self._Rectangle__height) is not int:
            raise TypeError("height must be an integer")
        if (self._Rectangle__height < 0):
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if type(self._Rectangle__width) is not int:
            raise TypeError("width must be an integer")
        if (self._Rectangle__width < 0):
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @width.setter
    def height(self, value):
        if type(self._Rectangle__height) is not int:
            raise TypeError("height must be an integer")
        if (self._Rectangle__height < 0):
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
