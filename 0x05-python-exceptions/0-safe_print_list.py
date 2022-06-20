#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x > len(my_list):
            raise IndexError
        for i in range((x - 1)):
            print(my_list[i], end="")
        print(my_list[x-1], end="\n")
        return x
    except(IndexError):
        for i in range((len(my_list) - 1)):
            print(my_list[i], end="")
        print(my_list[-1], end="\n")
        return len(my_list)
