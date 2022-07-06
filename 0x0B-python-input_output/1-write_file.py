#!/usr/bin/python3

"""
    a module for a function that appends data to a file
"""


def write_file(filename="", text=""):
    """
        write to:
        file by the name (filename)
        text - the content to write to the file
    """
    with open(filename, 'w+') as file:
        count = file.write(text)
        return count
