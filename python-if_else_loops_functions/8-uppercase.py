#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - ord('a') + ord('A'))
        print("{}".format(c), end="")
    print()
