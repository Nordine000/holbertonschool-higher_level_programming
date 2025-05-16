#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    newlist = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            newlist.append(res)
        except (ValueError, TypeError):
            res = 0
            newlist.append(res)
            print("wrong type")
            pass
        except ZeroDivisionError:
            res = 0
            newlist.append(res)
            print("division by 0")
            pass
        except IndexError:
            res = 0
            newlist.append(res)
            print("out of range")
        finally:
            pass

    return newlist
