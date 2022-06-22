#!/usr/bin/python3
"""
   a simple Square module
"""


class Square:
    """ This is a Square class that has private attributes or properties
        Attributes:
            __size (str): private attribute
    """
    __size = 0

    def __init__(self, _Square__size=0):
        Square.__size = self._Square__size = _Square__size
        if type(_Square__size) is not int:
            raise TypeError("size must be an integer")
        if _Square__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return Square.__size * Square.__size
