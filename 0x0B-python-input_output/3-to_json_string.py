#!/usr/bin/python3

import json

"""
    module for a function that returns
    the json form of an object
"""


def to_json_string(my_obj):
    """
        my_obj: the obj to serialize into json
    """
    json_object = json.dumps(my_obj)

    return str(json_object)
