#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nombre in matrix:
        for i in range(len(nombre)):
            if i != 0:
                print("", end="")
            print("{:d}".format(nombre[i]), end="")
        print()
