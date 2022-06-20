#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        if x > len(my_list):
            raise IndexError
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        return count
    except(IndexError):
        for val in my_list:
            print(val, end="")
        return len(my_list)
