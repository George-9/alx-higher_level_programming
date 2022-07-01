#!/usr/bin/python3
def remove_char_at(str, n):
    a = ''
    for incr in range(0, len(str)):
        if incr == n:
            continue
        else:
            a += str[incr]
    return a
