#!/usr/bin/python3
for i in range(1, 89):
    if i >= 10:
        if i > 10 and ((str(i)[0] == str(i)[1])):
            continue
        if int((str(i)[1] + str(i)[0])) > (int((str(i)[0] + str(i)[1]))):
            continue
    print("{:02d}".format(i), end=", ")
print("{:02d}".format(i + 1))
