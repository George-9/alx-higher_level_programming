#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for val in my_list:
            print(val, end="")
            counter += 1
    except IndexError:
        pass
    print()
    return counter
