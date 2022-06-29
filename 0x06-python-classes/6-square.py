#!/usr/bin/python3
"""
   a simple Square module
"""


class Square:
    """ This is a Square class that has private attributes or properties
        Attributes:
            __size (str): private attribute
    """
    def __init__(self, _Square__size=0, position=0):
        self.size = _Square__size
        self.position = position

    def area(self):
        if ((type(self.size)) is not int):
            raise TypeError("size must be an integer")

        if (self.size < 0):
            raise ValueError("size must be >= 0")

        return self.size * self.size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value=0):
        self.__size = value

    def my_print(self):
        if (self.size == 0):
            print()
        for i in range(self.size):
            print("#" * self.size)

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        if (type(self.__position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value
