#!/usr/bin/env python3


"""
Utile pour savoir le temps pris par mes fonctions
lors d'une execution
"""

import random as rd
from random import random
from sys import argv

def approximation_liste(nombre, taille):
    "approxime pi en fonction de n, retourne les points et dit s'ils sont dans le cercle"
    liste = nombre * [None]
    for k in range(nombre):
        x_abscisse = random()*2 -1
        y_abscisse = random()*2 -1
        if x_abscisse*x_abscisse + y_abscisse*y_abscisse <= 1:
            liste[k] = [int(x_abscisse*taille/2 + taille/2),
                         int(-y_abscisse*taille/2 + taille/2), True]
        else:
            liste[k] = [int(x_abscisse*taille/2 + taille/2),
                         int(-y_abscisse*taille/2 + taille/2), False]
    return liste

def approximation(nombre):
    "approxime pi en fonction de n"
    compteur = 0
    for _ in range(0, nombre):
        x_abscisse = rd.random()*2 -1
        y_abscisse = rd.random()*2 -1
        if x_abscisse*x_abscisse + y_abscisse*y_abscisse <= 1:
            compteur += 1
    return 4*compteur/nombre

def main_fonction(nombre):
    "approxime pi en fonction de n"
    compteur = 0
    for _ in range(0, nombre):
        x_abscisse = rd.random()*2 -1
        y_abscisse = rd.random()*2 -1
        if x_abscisse*x_abscisse + y_abscisse*y_abscisse <= 1:
            compteur += 1
    print(4*compteur/nombre)

if __name__ == "__main__":
    main_fonction(int(argv[1]))
