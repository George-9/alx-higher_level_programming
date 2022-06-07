#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    count = (len(my_list)) - 1
    for num in my_list:
        print('{:d}'.format(my_list[count]))
        count -= 1
