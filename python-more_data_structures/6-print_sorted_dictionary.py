#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    for key in a:
        print("{}: {}".format(key, a_dictionary[key]))