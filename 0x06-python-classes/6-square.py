#!/usr/bin/python3
"""Square module."""


class Square:
    """
    Defines a Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: lenght of the square.
            position: position of the square
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints in stdout the square with the char #"""
        if self.__size == 0:
            print()
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ") for j in range(self.__position[0])]
            [print("#") for k in range(self.__size)]
            print()

    @property
    def position(self):
        """Returns the position of the square
        Rteurns:
            the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the values of the position
        Args:
            value: the new value of the position
        Raises:
            TypeError: if the tuples values aren't positve integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value
