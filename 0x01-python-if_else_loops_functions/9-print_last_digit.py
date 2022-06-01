#!/usr/bin/python3
def print_last_digit(number):
    print("{:d}".format(number % 10), end="")
    return int(str(number)[-1])
