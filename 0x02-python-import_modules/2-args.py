#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    n = 1
    if len(argv) == 1:
        print('0 arguments.')
    if len(argv) == 2:
        print('1 argument:')
        print('{:d}: {}'.format(1, argv[1]))
    else:
        for arg in argv:
            if n > 1:
                print('{:d}: {}'.format(n, arg))
                n += 1
