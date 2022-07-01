#!/usr/bin/python3

"""
    a simple module for adding two integers and returning
    their sum as an int
"""


def add_integer(a, b=98):
    """
         return int
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("a must be an integer or b must be an integer")

    sum = int(a) + int(b)

    return sum
