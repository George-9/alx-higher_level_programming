#!/usr/bin/python3
def no_c(my_string):
    cont = ""
    for letter in my_string:
        if letter.lower() == 'c':
            continue
        cont += letter
    return cont
