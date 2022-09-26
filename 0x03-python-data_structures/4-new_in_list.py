#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx < 0 and idx > len(my_list):
            return my_list
        copy_list = [j for j in my_list]
        copy_list[idx] = element
        return copy_list
