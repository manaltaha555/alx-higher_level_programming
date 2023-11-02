#!/usr/bin/python3
""" Define properities and behaviours of the rectangle"""


class Regtangle:
    """Representation of a rectangle """
    def __init__(self, width=0, height=0):
        """initialize the rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rterieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
