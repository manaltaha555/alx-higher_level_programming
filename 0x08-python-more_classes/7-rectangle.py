#!/usr/bin/python3
"""Module for rectangle properties."""


class Rectangle:
    """Representation of a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Reterieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the preimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Return the rectangle shape."""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return ((str(Rectangle.print_symbol) * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Return representation of the Rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete the rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
