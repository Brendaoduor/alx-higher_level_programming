#!/usr/bin/python3
if __name__ == '__main__':
    """this program adds, subtracts, divides and multiplies two numbers"""
    from calculator_1 import add
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    
    from . import sub
    print("{} - {} = {}".format(a, b, add(a, b)))

    from . import mul
    print("{} * {} = {}".format(a, b, add(a, b)))

    from . import div
    print("{} / {} = {}".format(a, b, add(a, b)))
