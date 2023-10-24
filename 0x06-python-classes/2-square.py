#!/usr/bin/python3
"""Square module."""


class Square:
    """
    Defines a Square.
    """
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: lenght of the square.
        Raises:
            TypeError: if size isn't an integer
            ValueErro: if size si less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
