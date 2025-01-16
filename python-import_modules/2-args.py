#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv  # accès aux arguments de la ligne de commande
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(1, argc + 1):  # +1 = jusqu'a la fin
        print("{}: {}".format(i, argv[i]))  # position et valeur
