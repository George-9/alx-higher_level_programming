#!/usr/bin/python3
"""
    a simple python module about a rectangle class
"""


class Rectangle:
    """
        A rectangle object class
        Attributes: none
    """
    def __init__(self, width=0, height=0):
        """
            instantiate the rectangle object
        """
        self._Rectangle__height = height
        self._Rectangle__width = width

    @property
    def width(self):
        """
            returns the width of the rectangle
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
            sets the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
            returns the height of the rectangle
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
            sets the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def perimeter(self):
        """
           returns the perimeter of the rectangle
        """
        if (self._Rectangle__height == 0) or (self._Rectangle__width == 0):
            return 0
        return (self._Rectangle__height * 2)+(self._Rectangle__width * 2)

    def area(self):
        """
           returns the area of the rectangle
        """
        return (self._Rectangle__height * self._Rectangle__width)
