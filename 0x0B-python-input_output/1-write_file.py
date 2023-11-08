#!/usr/bin/python3
"""Module for write_file method."""


def write_file(filename="", text=""):
    """Write to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
