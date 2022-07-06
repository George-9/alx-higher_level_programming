#!/usr/bin/python3

import json

"""
    module for function that converts data from json to object
"""


def from_json_string(my_str):
    """
        my_str: the json object to convert
    """
    return json.loads(my_str)
