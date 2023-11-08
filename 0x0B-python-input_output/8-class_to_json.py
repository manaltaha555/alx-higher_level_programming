#!/usr/bin/python3
"""Maodule for class_to_json method."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
