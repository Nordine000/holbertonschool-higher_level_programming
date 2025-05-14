#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []

    for i in set_1:
        for i in set_2:
            common.append(i)
    return set(common)
