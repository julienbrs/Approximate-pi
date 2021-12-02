#!/usr/bin/env python3
# pylint: disable=too-many-locals


""" reçoit 3 arguments dans l'ordre suivant depuis la ligne de commande :
la taille de l'image en pixels, qui est carrée donc un seul entier qui devra être supérieur ou
égale à 100 ;
le nombre de point n à utiliser dans la simulation, qui devra être supérieur à 100 ;
le nombre de chiffres après la virgule à utiliser dans l'affichage de la valeur approximative
de π, qui devra être compris entre 1 et 5
"""
from sys import argv
import subprocess
import time
import approximate_pi

# https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/


def barre_horizontale(longueur, indice_depart):
    """longueur = longueur de la barre en pixels, départ = coord du pixel,
    la barre commencera de celui ci par son
    extrémité gauche; taille de l'image"""
    liste_indice = []
    liste_indice.append(indice_depart)
    for _ in range(longueur):
        indice_depart += 1
        liste_indice.append(indice_depart)

    indice_fin = liste_indice[-1]
    return liste_indice, indice_fin


def barre_verticale(hauteur, indice_depart, taille):
    """hauteur = hauteur de la barre en pixels, départ = coord du pixel,
    la barre commencera par son
    extrémité basse; taille de l'image"""
    liste_indice = []

    liste_indice.append(indice_depart)
    for _ in range(hauteur):
        indice_depart -= taille
        liste_indice.append(indice_depart)

    indice_fin = liste_indice[-1]
    return liste_indice, indice_fin


def chiffre_1(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 1"
    liste_indice, pointeur = barre_verticale(hauteur, indice_depart, taille)
    liste_indice += barre_verticale(hauteur, pointeur, taille)[0]
    return liste_indice

def chiffre_2(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 2"
    liste_indice = barre_horizontale(longueur, indice_depart)[0]
    liste_temp, pointeur = barre_verticale(hauteur, indice_depart, taille)
    liste_indice += liste_temp
    liste_temp, pointeur = barre_horizontale(longueur, pointeur)
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    pointeur = pointeur - longueur
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    return liste_indice

def chiffre_3(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 3"
    liste_indice, pointeur = barre_horizontale(longueur, indice_depart)
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    pointeur -= longueur
    liste_temp, pointeur = barre_horizontale(longueur, pointeur)
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    pointeur -= longueur
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    return liste_indice

def chiffre_4(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 4"
    indice_depart += longueur
    liste_indice, pointeur = barre_verticale(hauteur, indice_depart, taille)
    liste_temp = barre_verticale(hauteur, pointeur, taille)[0]
    liste_indice += liste_temp
    pointeur -= longueur
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    liste_temp = barre_verticale(hauteur, pointeur, taille)[0]
    liste_indice += liste_temp
    return liste_indice

def chiffre_5(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 5"
    liste_indice, pointeur = barre_horizontale(longueur, indice_depart)
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    pointeur -= longueur
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    return liste_indice


def chiffre_6(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 6"
    liste_indice, pointeur = barre_verticale(hauteur, indice_depart, taille)
    liste_temp = barre_verticale(hauteur, pointeur, taille)[0]
    liste_indice += liste_temp
    liste_temp, pointeur = barre_horizontale(longueur, indice_depart)
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    pointeur -= longueur
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    return liste_indice

def chiffre_7(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 7"
    indice_depart += longueur
    liste_indice, pointeur = barre_verticale(hauteur, indice_depart, taille)
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    pointeur -= longueur
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    return liste_indice

def chiffre_8(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 8"
    liste_indice, pointeur = barre_verticale(hauteur, indice_depart, taille)
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    liste_temp,pointeur = barre_horizontale(longueur, indice_depart)
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    liste_temp = barre_verticale(hauteur, pointeur, taille)[0]
    liste_indice += liste_temp
    return liste_indice

def chiffre_9(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 9"
    liste_indice, pointeur = barre_horizontale(longueur, indice_depart)
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    liste_temp = barre_verticale(hauteur, pointeur, taille)[0]
    liste_indice += liste_temp
    pointeur = pointeur - longueur
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    liste_temp, pointeur= barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    return liste_indice

def chiffre_0(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 0"
    liste_indice, pointeur = barre_horizontale(longueur, indice_depart)
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, indice_depart, taille)
    liste_indice += liste_temp
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
    liste_indice += liste_temp
    liste_temp = barre_horizontale(longueur, pointeur)[0]
    liste_indice += liste_temp
    return liste_indice


def ecrire_pi(approxpi, liste_image, pointeur, hauteur, longueur, taille):
    "ecrit les nombres"
    liste_indice_finale = []

    for k in range(len(str(approxpi))):
        pointeur += longueur + 3
        if str(approxpi)[k] == ".":
            liste_indice_finale.append(pointeur + 3)
        elif int(int(str(approxpi)[k])) == 1:
            liste_indice_finale += chiffre_1(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 2:
            liste_indice_finale += chiffre_2(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 3:
            liste_indice_finale += chiffre_3(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 4:
            liste_indice_finale += chiffre_4(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 5:
            liste_indice_finale += chiffre_5(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 6:
            liste_indice_finale += chiffre_6(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 7:
            liste_indice_finale += chiffre_7(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 8:
            liste_indice_finale += chiffre_8(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 0:
            liste_indice_finale += chiffre_0(hauteur, longueur, pointeur, taille)
        elif int(str(approxpi)[k]) == 9:
            liste_indice_finale += chiffre_9(hauteur, longueur, pointeur, taille)
    for chiffre in liste_indice_finale:
        liste_image[chiffre] = "Black"
    return liste_image


def conversion_en_px(taille, liste):
    "Convertie point dans [-1;1]² en coord px"
    liste_px = []
    for coord in liste:
        x_abs = int(coord[0]*taille/2 + taille/2)
        y_ord = int(-(coord[1]*taille/2 - taille/2))
        liste_px.append([x_abs,y_ord, coord[2]])
    return liste_px


def dictionnaire_none(taille):
    "crée un dictionnaire avec coord dans l'ordre et None en attribut"
    dictionnaire = {}
    for j in range(taille):
        for i in range(taille):
            string = str(i) + "," + str(j)
            dictionnaire[string] = None
    return dictionnaire


def ecrire_fichier(nom, taille, liste_image):
    "Ecrit dans le fichier l'image correspodante d'après la liste"
    with open(nom,'w', encoding='UTF-8') as fichier:
        fichier.write('P3\n')
        fichier.write(str(taille))
        fichier.write(" ")
        fichier.write(str(taille))
        fichier.write("\n255\n")
        for point in liste_image:
            if point is None:
                fichier.write("255 255 255\n")
            if point is True:
                fichier.write("0 255 0\n")    #Jaune
            elif point is False:
                fichier.write("255 0 0\n") #Rouge
            elif point == "Black":
                fichier.write("0 0 0\n") #Rouge


def generate_ppm_file(taille, nb_points_tot, nb_float):
    "genere le l'image, core de la fonction"
    # Conversion d'UA en pixels
    for repetition in range(1,11):
        nb_points = repetition*int(nb_points_tot/10)
        liste_debut, approxpi = approximate_pi.approximation(nb_points)
        approxpi = round(approxpi, nb_float)

        liste_px = conversion_en_px(taille, liste_debut)

        #création dictionnaire contenant coordonnée  + couleur (tout blanc à start)
        dictionnaire_points = dictionnaire_none(taille)

        #On change la couleur pour les points qui sont dans la liste_px
        for points in liste_px:
            #0 abscsse, 1 ord
            dictionnaire_points[str(points[0]) + "," + str(points[1])] = points[2]

        #Faire correspondance entre coord et index sur l'image:
        liste_image = taille**2 * [None]
        for coord in dictionnaire_points:
            x_abs, y_ord = int(str.split(coord, sep = ",")[0]), int(str.split(coord, sep = ",")[1])

            #indexpx = int(y_ord*taille + x+1)
            liste_image[y_ord*taille + x_abs] = dictionnaire_points[coord]

        #écriture de pi
        longueur = int(0.2*taille/(nb_float+1))
        hauteur = int(longueur*1.2)
        depart = int((taille/2)*taille + taille/4 +1 )
        liste_image_fin = ecrire_pi(approxpi, liste_image, depart, hauteur, longueur, taille)

        #Creation image
        chaine = ""
        liste_chiffre = [str(approxpi)[k] for k in range(1,len(str(approxpi)))]
        for k in range(1,len(liste_chiffre)):
            chaine += liste_chiffre[k]
        nom = f'image{repetition}_{str(approxpi)[0]}-{chaine}.ppm'
        ecrire_fichier(nom, taille, liste_image_fin)


def creation_gif(les_images):
    "créé un gif à partir des images"
    subprocess.call ("convert -delay 50 " + les_images + " legif.gif" , shell = True)


if __name__ == "__main__":
    #taille: argv[1], nbpoint: argv[2], nbfloat: argv[3]
    if int(argv[1])<100 or int(argv[2])<100 or 1 <=int(argv[1])<=5:
        raise ValueError
    start = time.time()
    generate_ppm_file(int(argv[1]),int(argv[2]), int(argv[3]))
    creation_gif("image*")
    end = time.time()
    temps_exec = end - start

print(f'Temps d\'exécution : {temps_exec:.2}ms')
