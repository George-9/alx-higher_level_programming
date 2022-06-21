#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter, nums_p = 0, 0
    try:
        for elem in my_list:
            counter += 1
        for val in my_list:
            print(val, end="")
            nums_p += 1
        print()
        return nums_p
    except IndexError:
        pass
    finally:
        return counter
