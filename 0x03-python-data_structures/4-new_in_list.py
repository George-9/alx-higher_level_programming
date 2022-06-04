#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    the_list = []
    for num in my_list:
        the_list.append(num)
    the_list[idx] = element
    return the_list
