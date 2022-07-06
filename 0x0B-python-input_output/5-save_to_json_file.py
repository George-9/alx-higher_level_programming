#!/usr/bin/python3

import json

"""
    module for writing json obj to a text file
"""


def save_to_json_file(my_obj, filename):
    """
       my_obj: object to write to file
       filename: name of the file
    """
    with open(filename, 'w+') as file:
        json.dump(my_obj, file)
