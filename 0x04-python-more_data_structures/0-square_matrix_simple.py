#!/usr/bin/python3
def mul(arr):
    nums = []
    for a in arr:
        nums.append(a * a)
    return nums


def square_matrix_simple(matrix=[]):
    container, arr = [], []
    arr = map(mul, matrix)
    return list(arr)
