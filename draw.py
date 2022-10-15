#!/usr/bin/env python3
# pylint: disable=too-many-arguments
#pylint: disable=too-many-locals

""" reçoit 3 arguments dans l'ordre suivant depuis la ligne de commande :
la taille de l'image en pixels, qui est carrée donc un seul entier qui devra être supérieur ou
égale à 100 ;
le nombre de point n à utiliser dans la simulation, qui devra être supérieur à 100 ;
le nombre de chiffres après la virgule à utiliser dans l'affichage de la valeur approximative
de π, qui devra être compris entre 1 et 5
"""

import sys
import subprocess
import approximate_pi


def barre_horizontale(longueur, indice_depart):
    """longueur = longueur de la barre en pixels, départ = coord du pixel,
    la barre commencera de celui ci par son
    extrémité gauche; taille de l'image"""
    liste_indice = [indice_depart]
    for _ in range(longueur):
        indice_depart += 1
        liste_indice.append(indice_depart)

    indice_fin = liste_indice[-1]
    return liste_indice, indice_fin


def barre_verticale(hauteur, indice_depart, taille):
    """hauteur = hauteur de la barre en pixels, départ = coord du pixel,
    la barre commencera par son
    extrémité basse; taille de l'image"""
    liste_indice = [indice_depart]
    for _ in range(hauteur):
        indice_depart -= taille
        liste_indice.append(indice_depart)

    indice_fin = liste_indice[-1]
    return liste_indice, indice_fin


def chiffre_1(hauteur, longueur, indice_depart, taille):
    "écrit le chiffre 1"

    liste_indice, pointeur = barre_verticale(hauteur, indice_depart, taille)
    liste_indice += barre_verticale(hauteur, pointeur, taille)[0]
    taille = longueur
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
    liste_temp, pointeur = barre_horizontale(longueur, indice_depart)
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
    liste_temp, pointeur = barre_verticale(hauteur, pointeur, taille)
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
    dictionnaire_fonction = {}
    dictionnaire_fonction[0] = chiffre_0
    dictionnaire_fonction[1] = chiffre_1
    dictionnaire_fonction[2] = chiffre_2
    dictionnaire_fonction[3] = chiffre_3
    dictionnaire_fonction[4] = chiffre_4
    dictionnaire_fonction[5] = chiffre_5
    dictionnaire_fonction[6] = chiffre_6
    dictionnaire_fonction[7] = chiffre_7
    dictionnaire_fonction[8] = chiffre_8
    dictionnaire_fonction[9] = chiffre_9
    for k in range(len(str(approxpi))):
        pointeur += longueur + 6
        if str(approxpi)[k] == ".":
            liste_indice_finale.append(pointeur + 3)
        else:
            liste_indice_finale += dictionnaire_fonction[int(str(approxpi)[k])](hauteur,
             longueur, pointeur, taille)

    for chiffre in liste_indice_finale:
        liste_image[chiffre] = "Black"
    return liste_image

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
    with open(nom, 'w', encoding='UTF-8') as fichier:
        fichier.write('P2\n')
        fichier.write(str(taille))
        fichier.write(" ")
        fichier.write(str(taille))
        fichier.write(" 3\n")
        for point in liste_image:
            if point is None:
                fichier.write("1\n")
            if point is True:
                fichier.write("2\n")    #Jaune
            elif point is False:
                fichier.write("3\n") #Rouge
            elif point == "Black":
                fichier.write("0\n") #Rouge


def generate_ppm_file(taille, nb_points_tot, nb_float):
    "genere le l'image, core de la fonction"
    # Conversion d'UA en pixels
    liste_image = taille*taille * [None]
    dictionnaire_points = dictionnaire_none(taille)
    longueur = int(0.2*taille/(nb_float+1))
    hauteur = int(longueur*1.2)
    depart = int((taille/2)*taille + taille/3 +1)
    for repetition in range(0, 10):
        approxpi = approximate_pi.approximation(int(nb_points_tot/10)*(repetition+1))
        liste_px = approximate_pi.approximation_liste(int(nb_points_tot/10), taille)
        approxpi = round(approxpi, nb_float)
        #création dictionnaire contenant coordonnée  + couleur (tout blanc à start)


        #On change la couleur pour les points qui sont dans la liste_px
        for points in liste_px:
            #0 abscsse, 1 ord
            dictionnaire_points[str(points[0]) + "," + str(points[1])] = points[2]
        #Faire correspondance entre coord et index sur l'image:
        for coord in dictionnaire_points:
            x_abs, y_ord = int(str.split(coord, sep=",")[0]), int(str.split(coord, sep=",")[1])

            #inprint(f'Temps d\'exécution : {temps_exec:.2}ms')dexpx = int(y_ord*taille + x+1)
            liste_image[y_ord*taille + x_abs] = dictionnaire_points[coord]

        #écriture de pi
        liste_image_chiffre = ecrire_pi(approxpi, liste_image, depart, hauteur, longueur, taille)
        #Creation image
        chaine = ""
        liste_chiffre = [str(approxpi)[k] for k in range(1, len(str(approxpi)))]
        for k in range(1, len(liste_chiffre)):
            chaine += liste_chiffre[k]
        nom = f'img{repetition}_{str(approxpi)[0]}-{chaine}.ppm'
        ecrire_fichier(nom, taille, liste_image_chiffre)


def creation_gif(les_images):
    "créé un gif à partir des images"
    subprocess.call("convert -delay 50 " + les_images + " result.gif", shell=True)

def main():
    "main"
    #taille: argv[1], nbpoint: argv[2], nbfloat: argv[3], clean: argv[4]
    if len(sys.argv) != 4:
        print("Erreur, il faut 3 arguments: taille, nb_points, nb_float")
        sys.exit(1)

    elif int(sys.argv[1]) < 100 or int(sys.argv[2]) < 100 or not 1 <= int(sys.argv[3]) <= 5:
        raise ValueError

    elif len(sys.argv) == 4 or sys.argv[5] != "false":
        subprocess.call("rm result_images/img*.ppm", shell=True)
        subprocess.call("rm result.gif", shell=True)

    generate_ppm_file(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    creation_gif("img*")
    subprocess.call("mv img* result_images", shell=True)



if __name__ == "__main__":
    main()
