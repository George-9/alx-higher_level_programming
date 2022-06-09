#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda sub_arr: list(map(lambda a: a * a, sub_arr)), arr))
