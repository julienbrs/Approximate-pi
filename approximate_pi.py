#!/usr/bin/env python3

"""

Script that can approximate pi using the Monte Carlo method, and can
also return the points and tell if they are in the circle or not

"""

import random as rd
from random import random
from sys import argv

def list_approximation(number, taille):
    "approximate pi as a function of n, return the points and tell if they are in the circle"
    liste = number * [None]
    for k in range(number):
        x_abscissa = random()*2 -1
        y_abscissa = random()*2 -1
        if x_abscissa*x_abscissa + y_abscissa*y_abscissa <= 1:
            liste[k] = [int(x_abscissa*taille/2 + taille/2),
                         int(-y_abscissa*taille/2 + taille/2), True]
        else:
            liste[k] = [int(x_abscissa*taille/2 + taille/2),
                         int(-y_abscissa*taille/2 + taille/2), False]
    return liste

def approximation(number):
    " approximate pi as a function of n"
    compteur = 0
    for _ in range(0, number):
        x_abscissa = rd.random()*2 -1
        y_abscissa = rd.random()*2 -1
        if x_abscissa*x_abscissa + y_abscissa*y_abscissa <= 1:
            compteur += 1
    return 4*compteur/number

if __name__ == "__main__":
    # If called as a script, print the approximation of pi
    print(approximation(int(argv[1])))
