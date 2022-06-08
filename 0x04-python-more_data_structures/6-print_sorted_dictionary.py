#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    map_list = []
    keys = list(sorted(a_dictionary))
    for elem in keys:
        map_list.append({elem: a_dictionary[elem]})
    for val in map_list:
        print('{}: {}'.format(list(val.keys())[0], list(val.values())[0]))
