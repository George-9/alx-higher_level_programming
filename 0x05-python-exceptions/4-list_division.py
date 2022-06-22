#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    cont = []
    for r in range(list_length):
        try:
            if (my_list_1[r] % my_list_2[r]) != 0:
                cont.append(0)
            cont.append((my_list_1[r] / my_list_2[r]))
        except (IndexError):
            print("out of range")
        except (TypeError):
            cont.append(0)
            print("wrong type")
        except (ZeroDivisionError):
            cont.append(0)
            print("division by 0")
        finally:
            diff = len(cont) - list_length
    if diff < 0:
        for num in range(diff * -1):
            cont.append(0)
    return cont
