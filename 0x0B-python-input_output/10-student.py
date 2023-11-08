#!/usr/bin/python3
"""Module fo calss student."""


class Student:
    """Define class student."""

    def __init__(self, first_name, last_name, age):
        """Initaiation of attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary represenation of a student."""
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
