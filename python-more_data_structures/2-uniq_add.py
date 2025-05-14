#!/usr/bin/python3
def uniq_add(my_list=[]):
    element = []
    resultat = 0
    for nombre in my_list:
        if nombre not in element:
            element.append(nombre)
            resultat += nombre
    return resultat
