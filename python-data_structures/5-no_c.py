#!/usr/bin/python3
def no_c(my_string):
    new_chaine = ""
    for le_caractere in my_string:
        if le_caractere != "c" or le_caractere != "C":
            new_chaine += le_caractere
            print(new_chaine)
