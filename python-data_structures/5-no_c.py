#!/usr/bin/python3
def no_c(my_string):
    po = ''
    for i in my_string:
        if i not in ('C','c'):
        po += i

        return po
