#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique = []
    for elem in set_1:
        if elem not in unique:
            unique.append(elem)
    for elem in set_2:
        if elem not in unique:
            unique.append(elem)
    return unique
