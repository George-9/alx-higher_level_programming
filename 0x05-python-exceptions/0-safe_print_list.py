#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter, nums_p = 0, 0
    try:
        for elem in my_list:
            counter += 1
        if x > counter:
            raise IndexError
        if x == 0:
            print(my_list[0], end="\n")
            return 1
        for i in range((x - 1)):
            print(my_list[i], end="")
            nums_p += 1
        nums_p += 1
        print(my_list[(x - 1)], end="\n")
        return nums_p
    except IndexError:
        pass
    finally:
        return counter
