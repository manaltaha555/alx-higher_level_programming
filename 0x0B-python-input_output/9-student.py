#!/usr/bin/python3
"""Module fo calss student."""


class Student:
    """Define class student."""

    def __init__(self, first_name, last_name, age):
        """Initaiation of attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary represenation of a student."""
        return self.__dir__
