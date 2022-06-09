#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return None
    item, total, l_val = (0, 0), 0, 0
    for _tuple in my_list:
        item = (_tuple + (0, 0))
        total += (item[0] * item[1])
        l_val += item[1]
    return total / l_val
