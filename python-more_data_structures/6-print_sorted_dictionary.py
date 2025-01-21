#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    for keys in a:
        print("{}: {}".format(keys, a_dictionary[keys]))
