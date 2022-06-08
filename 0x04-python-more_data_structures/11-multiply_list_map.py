#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mul_arr = []
    for val in my_list:
        mul_arr.append(val * number)
    return mul_arr
