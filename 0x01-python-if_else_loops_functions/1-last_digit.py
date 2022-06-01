#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(str(number)[(len(str(number))) - 1])
l_pp = "and is less than 6 and is not 0"
p = "Last digit of"
l_p = "and is less than 6 and not 0"
if l_digit == 0:
    print("Last digit of {:d} is {l_digit:d} and is 0".format(number))
elif number < 0:
    print(f"{p} {:d} is {l_digit * -1:d} {l_p}".format(number))
elif number > 0 and l_digit > 5:
    print(f"{p} {:d} is {l_digit:d} and is greater than 5".format(number))
else:
    print(f"{p} {:d} is {l_digit:d} {l_pp}".format(number))
