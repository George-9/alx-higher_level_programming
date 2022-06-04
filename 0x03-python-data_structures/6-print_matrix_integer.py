#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for num in arr:
            if arr.index(num) == len(arr) - 1:
                print('{:d}'.format(num), end="")
            else:
                print('{:d} '.format(num), end="")
        print()
