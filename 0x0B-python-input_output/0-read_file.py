#!/usr/bin/python3
"""Modulel for read_file method."""


def read_file(filename=""):
    """Read the file."""
    with open(filename, 'r') as file:
        file_content = file.read()
        print(file_content, end="")
