#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for cles in sorted(a_dictionary):
        print(f"{cles}: {a_dictionary[cles]}")
