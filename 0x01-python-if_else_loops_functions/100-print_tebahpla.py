#!/usr/bin/python3
"""
    print alphabets in reverse interchanging case
"""

start, a, loop = 0, 0,122

while loop >= 97:
    if loop % 2 == 0:
        a, start = 0, 0
    else:
        start, a = 32, 64
    print(chr(((loop + start) - a)), end="")
    loop -= 1
