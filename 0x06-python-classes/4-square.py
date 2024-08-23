#!/usr/bin/python3
"""class square that defines a square"""

class Square:
    """class square that defines a square"""
    def __init__(self, size = 0):
        """This initializes the square

        Args:
            value(int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """retrieves the value

        Returns:
            private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size value

        Args:
            value (int): size of the square.
        """
         if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value #: size of the square

    def area(self):
        """returns the area of the square

        Returns:
            area.
        """
        return self.__size**2

