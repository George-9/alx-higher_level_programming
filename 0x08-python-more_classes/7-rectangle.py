#!/usr/bin/python3
"""
    a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
"""


class Rectangle:
    number_of_instances = 0
    """
        Attributes:
            number_of_instances (int): count number of class instances
    """
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1

        self._Rectangle__height = height
        self._Rectangle__width = width

        self.symbol = "#"

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if type(val) is not int:
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")

        self._Rectangle__height = value

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return (self._Rectangle__width * 2) + (self._Rectangle__height * 2)

    def __str__(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return ''
        rect = ''
        cont = ''
        for i in range(self._Rectangle__height):
            rect += (f"{self.print_symbol}" * self._Rectangle__width)
            rect += '\n'
        for a in range(len(rect) - 1):
            cont += rect[a]
        return cont

    @property
    def print_symbol(self):
        return self.symbol

    @print_symbol.setter
    def print_symbol(self, val):
        self.symbol = val

    def __repr__(self):
        w, h = self._Rectangle__width, self._Rectangle__height
        return f'Rectangle({w}, {h})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
