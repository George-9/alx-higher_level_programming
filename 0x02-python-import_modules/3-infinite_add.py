#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    count, sum = 0, 0
    for num in argv:
        if count > 0:
            sum += int(num)
        count += 1
    print('{:d}'.format(sum))
