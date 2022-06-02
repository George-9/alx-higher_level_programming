#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4 as hid
    for line in (dir(hid)):
        if line.startswith('__') == False:
            print('{}'.format(line))
