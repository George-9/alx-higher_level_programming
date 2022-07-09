#!/usr/bin/python3

"""
    module for checkingattributes and methods of an object.
"""


def lookup(obj):
    """
        returns a list of attributes of the given object (obj)
    """
    return list(dir(obj))
