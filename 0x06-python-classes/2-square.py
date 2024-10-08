#!/usr/bin/python3
"""class square that defines a square"""

class Square:
    """class square that defines a square"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >=0')
        else:
            self.__size = size #:this is size of the square
