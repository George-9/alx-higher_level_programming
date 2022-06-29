#!/usr/bin/python3
"""
   a simple Square module
"""


class Square:
    """ This is a Square class that has private attributes or properties
        Attributes:
            __size (str): private attribute
    """
    def __init__(self, _Square__size=0):
        if ((type(_Square__size)) is not int):
            raise TypeError("size must be an integer")

        if (_Square__size < 0):
            raise ValueError("size must be >= 0")
        self.size = _Square__size

    def area(self):
        if ((type(self.size)) is not int):
            raise TypeError("size must be an integer")
        return self.size * self.size

        if (int(self.size) < 0):
            raise ValueError("size must be >= 0")

