#!/usr/bin/env python3

""" Hello """
from random import uniform
from sys import argv
#import time

def approximation_liste(nombre):
    "approxime pi en fonction de n, retourne les points et dit s'ils sont dans le cercle"
    liste = []
    compteur = 0
    for _ in range(0, nombre):
        x_abscisse = uniform(-1, 1)
        y_abscisse = uniform(-1, 1)
        if x_abscisse**2 + y_abscisse**2 <= 1:
            liste.append([x_abscisse, y_abscisse, True])
            compteur += 1
        else:
            liste.append([x_abscisse, y_abscisse, False])
    return liste, 4*compteur/nombre

def main(nombre):
    "approxime pi en fonction de n"
    compteur = 0
    for _ in range(0, nombre):
        x_abscisse = uniform(-1, 1)
        y_abscisse = uniform(-1, 1)
        if x_abscisse**2 + y_abscisse**2 <= 1:
            compteur += 1
    return 4*compteur/nombre

#def calcul_pi(nombre, compteur_ancien, repetition):
#    "approxime pi en fonction de n"
#    compteur = 0
#    print(compteur_ancien)
#    print(nombre)
#    print(nombre*repetition)
#    for _ in range(0, nombre):
#        x_abscisse = uniform(-1, 1)
#        y_abscisse = uniform(-1, 1)
#        if x_abscisse**2 + y_abscisse**2 <= 1:
#            compteur += 1
#    compteur += compteur_ancien
#    print("---")
#    return 4*compteur/(repetition*nombre), compteur

if __name__ == "__main__":
    main(int(argv[1]))
