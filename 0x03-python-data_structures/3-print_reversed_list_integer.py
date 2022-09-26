#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        if isinstance(my_list, list):
            print("{:d}".format(i))
