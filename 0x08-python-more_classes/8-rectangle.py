#!/usr/bin/python3
"""
    a simple python module about a rectangle class
"""


class Rectangle:
    """
        Attributes:
            number_of_instances (int): count number of class instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self._Rectangle__height = height
        self._Rectangle__width = width
        self.symbol = "#"

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
        if (self._Rectangle__width < 0):
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
           sets the height of the Rcanlge object
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (self._Rectangle__height < 0):
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        """
           returns the area of the Rectangle
        """
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        """
           returns the perimeter of the Rectangle object
        """
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return (self._Rectangle__width * 2) + (self._Rectangle__height * 2)

    @property
    def print_symbol(self):
        """
            returns the currently set symbol for the object
        """
        return self.symbol

    @print_symbol.setter
    def print_symbol(self, val):
        """
            sets the symbol for the object
        """
        self.symbol = val

    def __str__(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return ''
        rect = ''
        cont = ''
        for i in range(self._Rectangle__height):
            rect += ((str(self.print_symbol)) * self._Rectangle__width)
            rect += '\n'
        for a in range(len(rect) - 1):
            cont += rect[a]
        return cont

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            compares the areas of the two rectangles(rect_1 and rect_2) and
            returns the one with the bigger area

            if both are equal returns rect_1
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def __repr__(self):
        w, h = self._Rectangle__width, self._Rectangle__height
        return f'Rectangle({w}, {h})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
