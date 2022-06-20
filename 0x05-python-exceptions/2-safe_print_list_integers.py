#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for elem in my_list:
            counter += 1
        if x < 0 or x > counter:
            raise IndexError
        if x == 0:
            print(my_list[0], end="\n")
            return 1
        for i in range((x - 1)):
            print(my_list[i], end="")
        print(my_list[(x - 1)], end="\n")
        return x
    except(IndexError):
        count, counter = 0, 0
        for elem in my_list:
            counter += 1
        for val in range(counter - 1):
            print(my_list[val], end="")
        print(my_list[-1], end="\n")
        return counter
