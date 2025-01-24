def safe_print_list_integers(my_list=[], x=0):
    count = 1
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 0
        except (ValueError, TypeError):
            pass
    print()
    return count
