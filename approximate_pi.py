#!/usr/bin/env python3

""" Hello """
from random import uniform
from sys import argv

def approximation(n):
    "approxime pi en fonction de n, retourne les points et dit s'ils sont dans le cercle"
    L = []
    compteur = 0
    for _ in range(0,n):
        x_abscisse = uniform(-1, 1)
        y_abscisse = uniform(-1, 1)
        if x_abscisse**2 + y_abscisse**2 <= 1:
            L.append([x_abscisse, y_abscisse, True])
            compteur += 1
        else:
            L.append([x_abscisse, y_abscisse, False])
    return L, 4*compteur/n

def main():
    return approximation(int(argv[1]))


if __name__ == "__main__":
    print(approximation(int(argv[1])))
