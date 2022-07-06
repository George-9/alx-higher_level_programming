#!/usr/bin/python3

"""
    module for funtion that appends data to a given
    file
"""


def append_write(filename="", text=""):
    """
        finamae: name of the file
        text: content to write to the file
    """
    with open(filename, 'a+') as file:
        dataCount = file.write(text)
        return dataCount
