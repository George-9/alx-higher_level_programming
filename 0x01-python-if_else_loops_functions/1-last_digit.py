#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(str(number)[(len(str(number))) - 1])
l_pp = "and is less than 6 and is not 0"
p = "Last digit of"
l_p = "and is less than 6 and not 0"
if l_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, l_digit))
elif number < 0:
    print("{} {:d} is {:d} {}".format(p, number, l_digit * -1, l_p))
elif number > 0 and l_digit > 5:
    print("{} {:d} is {:d} and is greater than 5".format(p, number, l_digit))
else:
    print("{p} {:d} is {:d} {}".format(p, number, l_digit, l_pp))
