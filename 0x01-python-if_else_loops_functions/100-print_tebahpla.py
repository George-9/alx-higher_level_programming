#!/usr/bin/python3

i = 122

while(i >= ord('a')):
    if i % 2 != 0:
        print(chr(i).upper(), end="")
    else:
        print(chr(i), end="")
    i -= 1
