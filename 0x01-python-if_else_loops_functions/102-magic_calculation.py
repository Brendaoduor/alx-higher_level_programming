#!/usr/bin/python3
def magic_calculations(a, b, c):
    if (a < b) and (a < c):
        return c
    if (c > b) and (c > a):
        return(a + b)
    return(a*b - c)
