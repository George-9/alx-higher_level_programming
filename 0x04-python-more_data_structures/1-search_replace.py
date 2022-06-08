#!/usr/bin/python3
def search_replace(my_list, search, replace):
    container = []
    for num in my_list:
        if num == search:
            container.append(replace)
        else:
            container.append(num)
    return container
