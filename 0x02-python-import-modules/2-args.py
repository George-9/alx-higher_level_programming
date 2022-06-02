#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    n = 1
    if len(argv) == 1:
        print('0 arguments.')
    if len(argv) > 1:
        print('{:d} arguments:'.format(len(argv) - 1))
        for arg in argv:
            if argv.index(arg) >= 1:
                print('{:d}: {}'.format(n, arg))
                n += 1
