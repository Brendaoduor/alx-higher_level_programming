#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list[::-1]:
        print(i)

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
