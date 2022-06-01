#!/usr/bin/python3
def uppercase(str):
    a = ""
    for letter in str:
        if letter != ' ' and (ord(letter) - 32) >= 65:
            a += (chr(ord(letter) - 32))
        else:
            a += (chr(ord(letter)))
    print("{}".format(a))
