#!/usr/bin/python3
for i in range(1, 89):
    if (i % i - 1) == 0:
        continue
    print("{:02d}".format(i), end=", ")
print("{:02d}".format(i + 1))
