#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif a_dictionary is not None:
        max_key, max_num = '', 0
        for key in list(a_dictionary.keys()):
            if a_dictionary[key] > max_num:
                max_key = key
                max_num = a_dictionary[key]
    else:
        return None
    return max_key
