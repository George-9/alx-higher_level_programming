#!/usr/bin/python3

import json

"""
    a module with one function for loading json object from a given filename
"""


def load_from_json_file(filename):
    """
        load and return json object from file (filename)
    """
    obj = None

    with open(filename, 'r+') as file:
        obj = json.loads(file.read())

    return obj
