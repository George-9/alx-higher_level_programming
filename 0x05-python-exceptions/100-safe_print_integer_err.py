#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except ValueError as err:
        from sys import stderr 
        print("Exception: " + str(err), file=stderr)
        return False
    except TypeError as err:
        print("Exception:",  err)
        return False
