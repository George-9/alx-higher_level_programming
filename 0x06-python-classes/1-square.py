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

    def __init__(self, _Square__size):
        Square.__size = self._Square__size = _Square__size
