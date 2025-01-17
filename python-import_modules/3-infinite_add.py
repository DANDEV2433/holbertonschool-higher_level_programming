#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    total = 0
    argv = sys.argv  # accès aux arguments ligne de commande
    argc = len(argv) - 1
    for i in range(1, argc + 1):
        total += int(argv[i])  # Conversion arg en entier et ajout au total
    print(total)
