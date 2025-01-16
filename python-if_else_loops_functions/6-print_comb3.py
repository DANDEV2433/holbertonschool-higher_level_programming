#!/usr/bin/python3
for i in range(1, 90):
    if i == 89:
        print("{:02}".format(i))
    else:
        print("{:02}".format(i), end=", ")
