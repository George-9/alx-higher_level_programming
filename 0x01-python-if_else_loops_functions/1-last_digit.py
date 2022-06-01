#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int((str(number))[(len(str(number))) - 1])
print(number)

if last_digit == 0:
	print(f"Last digit of {number:d} is {last_digit:d} and is 0")

elif number < 0:
	print(f"Last digit of {number:d} is {last_digit * -1:d} and is less than 6 and is not 0")

elif number > 0 and last_digit > 5:
	print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
else:
        print(f"Last digit of {number:d} is {last_digit:d} and is less than 6 and is not 0")

