#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    cont = []
    for r in range(list_length):
        try:
            cont.append((my_list_1[r] / my_list_2[r]))
        except (IndexError):
            print("out of range")
        except (ZeroDivisionError):
            cont.append(0)
            print("division by 0")
        except (TypeError):
            cont.append(0)
            print("wrong type")
        finally:
            pass
    return cont
