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

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return (self._Rectangle__width * 2) + (self._Rectangle__height * 2)

    def __str__(self):
        rect = ''
        cont = ''
        for i in range(self._Rectangle__height):
            rect += ("#" * self._Rectangle__width)
            rect += '\n'
        for a in range(len(rect) - 1):
            cont += rect[a]
        return cont
 
