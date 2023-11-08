#!/usr/bin/python3
"""Module for from_json_string method."""
import json


def from_json_string(my_str):
    """Return the python object."""
    return json.loads(my_str)
