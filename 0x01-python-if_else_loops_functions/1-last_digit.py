#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int((str(number))[(len(str(number))) - 1])
p = "Last digit of"
l_p = "and is less than 6 and is not 0"
if l_digit == 0:
    print(f"Last digit of {number:d} is {l_digit:d} and is 0")
elif number < 0:
    print(f"{p} {number:d} is {l_digit * -1:d} {l_p}")
elif number > 0 and l_digit > 5:
    print(f"{p} {number:d} is {l_digit:d} and is greater than 5")
else:
    print(f"{p} {number:d} is {l_digit:d} and is less than 6 and is not 0")
