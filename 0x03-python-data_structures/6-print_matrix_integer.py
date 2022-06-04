#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        loop = 0
        for arr in matrix:
            for num in arr:
                print(' {:d}'.format(num), end="")
                loop += 1
            print()
