#!/usr/bin/python3
def element_at(my_list, idx):
    print(*my_list, sep="\n")
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
