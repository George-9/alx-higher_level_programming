#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
        if (idx < 0) or (idx > ((len(my_list) - 1))):
            return my_list
        count, list = 0, []
        for num in my_list:
            if count != idx:
                list.append(num)
            count += 1
        my_list.clear()
        for num in list:
            my_list.append(num)
        my_list = list
        return list
