#!/usr/bin/python3
"""class rectangle that defines rectangle"""

class Rectangle:
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ init rectangle

        Args:
            value (int): width and height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: private width.

        Returns:
            Private width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value of width, must be int.

        Args:
            value (int): width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """int: private height.

        Returns:
            Private height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value into height, must be int.

        Args:
            value (int): height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """returns the rectangle with the character #"""
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

   def __repr__(self):
       """returns a string representation of the rectangle"""
          return "Rectangle({}, {})".format(self.__width, self.__height)
