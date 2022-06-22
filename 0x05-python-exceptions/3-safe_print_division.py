#!/usr/bin/python3
def safe_print_division(a, b):
    val = 0
    try:
        val = a / b
        return val
    except ValueError:
        return None
    except ZeroDivisionError:
        val = None
        return None
    finally:
        print("Inside result: {}".format(val))
