#!/usr/bin/python3

a = ''

for i in range(97, 123):
    if i % 2 != 0:
        a += chr(i).upper()
    else:
        a += chr(i)

print(a[::-1])
