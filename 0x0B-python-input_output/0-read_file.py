#!/usr/bin/python3

"""
    module with function for reading file and
    prints the content in UTF-8 to the STDOUT
"""


def read_file(filename=""):
    """
        open file (filename)
        and read it's content
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data, end="")
