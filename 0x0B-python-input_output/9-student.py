#!/usr/bin/python3

"""
    a module for a Student class
"""


class Student(dict):
    """
        Attributes:
            first_name - student's first name
            last_name - student's last name
            age - students age
    """
    def __init__(self, first_name, last_name, age):
        """
            initialize object and set it's properties
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            a method that returns a json representation of
            the student object
        """
        f_name, l_name = self.first_name, self.last_name
        return '{"first_name": f_name, "last_name": l_name, "age": self.age}'
