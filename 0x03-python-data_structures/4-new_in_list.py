#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        if idx < 0 | idx > len(my_list):
            return my_list
        copy_list = list(my_list)
        copy_list[idx] = element
        return copy_list
