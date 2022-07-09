"""
    a module for with one metho that checks instances
"""


def is_same_class(obj, a_class):
    """
       returns True if obj is the same type as class otherwise returns False
    """
    return str(type(obj)) == str(a_class)
