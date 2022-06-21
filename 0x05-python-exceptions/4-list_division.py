#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    loop, cont = 0, []
    try:
        if list_length > len(my_list1) or list_length > len(my_list2):
            raise IndexError
        for r in range(list_length):
            cont.append((my_list1[r] / 2))
            cont.append((my_list2[r] / 2))
        return cont
    except (IndexError):
        print("out of range")
    except (ZeroDivisionError):
        print("division by 0")
    except (TypeError):
        print("wrong type")
    finally:
        return cont
