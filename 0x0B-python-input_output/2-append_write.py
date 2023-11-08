#!/usr/bin/python3
"""Module for append_write method."""


def append_write(filename="", text=""):
    """Append to a file."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
