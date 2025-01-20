#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, number in enumerate(line):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(number), end="")
        print()
