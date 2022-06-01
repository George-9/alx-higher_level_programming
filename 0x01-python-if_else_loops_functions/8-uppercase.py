#!/usr/bin/python3
def uppercase(str):
    a = ""
    for letter in str:
        a += chr(ord(letter))
    return a
