#!/usr/bin/python3
"""Module for load_from_json_file method."""
import json


def load_from_json_file(filename):
    """Create an object from a json file."""
    with open(filename, 'r') as f:
        return json.load(f)
