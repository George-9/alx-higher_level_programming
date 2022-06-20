#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for elem in my_list:
            counter += 1
        if x > counter:
            raise IndexError
        for i in range((x - 1)):
            print(my_list[i], end="")
        print(my_list[x-1], end="\n")
        return x
    except(IndexError):
        count = 0
        for val in my_list:
            count += 1
            print(val, end="")
            if my_list[count] == my_list[-1]:
                break
        count += 1
        print(my_list[-1], end="\n")
        return count
