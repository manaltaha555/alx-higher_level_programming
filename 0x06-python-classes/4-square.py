#!/usr/bin/python3
"""Square module."""


class Square:
    """
    Defines a Square.
    """
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: lenght of the square
        """
        self.__size = size

    def area(self):
        """Area of this square
        Returns:
            the square of this size
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter of size
        Returns:
            size of the instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size
        Args:
            value: the new value of the size
        Raises:
            TypeError: if size isn't an integer
            ValueErro: if size si less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
