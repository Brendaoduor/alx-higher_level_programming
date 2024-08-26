#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""

class Rectangle:
    """a class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ init rectangle

        Args:
            value (int): width and height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: private width

        Returns:
            private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value into width, must be int.

        Args:
            value (int): width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value #: width of the rectangle

    @property
    def height(self):
        """int: private height

        Returns
            private height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets value of the height, must be int.

        Args:
            value (int): height of rectangle.
        """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value #: height of the rectangle
