#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx < 0 and idx > (len(my_list) - 1):
            return my_list
        else:
            elem = [element if item == idx else item for item in my_list]
            return elem