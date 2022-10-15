#!/usr/bin/env python3
# pylint: disable=too-many-arguments
#pylint: disable=too-many-locals

""" receives 3 arguments in the following order from the command line:
the size of the image in pixels, which is square so a single integer that must be greater than or
equal to 100 ;
the number of points n to use in the simulation, which must be greater than 100;
the number of digits after the decimal point to be used in the display of the approximate value
of π, which must be between 1 and 5

"""

import sys
import subprocess
import approximate_pi


def horizontal_bar(length, start_index):
    """ length = length of the bar in pixels, start = coord of the pixel,
    the bar will start from this one by its left end; size of the output image"""
    list_index = [start_index]
    for _ in range(length):
        start_index += 1
        list_index.append(start_index)

    end_index = list_index[-1]
    return list_index, end_index


def vertical_bar(height, start_index, size):
    """ height = height of the bar in pixels, start = coordinate of the pixel,
    the bar will start at its bottom end; size of the output image
    """
    list_index = [start_index]
    for _ in range(height):
        start_index -= size
        list_index.append(start_index)

    end_index = list_index[-1]
    return list_index, end_index


def digit_1(height, _ , start_index, size):
    "write  digit 1"

    list_index, pointeur = vertical_bar(height, start_index, size)
    list_index += vertical_bar(height, pointeur, size)[0]
    return list_index

def digit_2(height, length, start_index, size):
    "write  digit 2"
    list_index = horizontal_bar(length, start_index)[0]
    list_temp, pointeur = vertical_bar(height, start_index, size)
    list_index += list_temp
    list_temp, pointeur = horizontal_bar(length, pointeur)
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    pointeur = pointeur - length
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    return list_index

def digit_3(height, length, start_index, size):
    "write  digit 3"
    list_index, pointeur = horizontal_bar(length, start_index)
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    pointeur -= length
    list_temp, pointeur = horizontal_bar(length, pointeur)
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    pointeur -= length
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    return list_index

def digit_4(height, length, start_index, size):
    "write  digit 4"
    start_index += length
    list_index, pointeur = vertical_bar(height, start_index, size)
    list_temp = vertical_bar(height, pointeur, size)[0]
    list_index += list_temp
    pointeur -= length
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    list_temp = vertical_bar(height, pointeur, size)[0]
    list_index += list_temp
    return list_index

def digit_5(height, length, start_index, size):
    "write  digit 5"
    list_index, pointeur = horizontal_bar(length, start_index)
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    pointeur -= length
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    return list_index


def digit_6(height, length, start_index, size):
    "write  digit 6"
    list_index, pointeur = vertical_bar(height, start_index, size)
    list_temp = vertical_bar(height, pointeur, size)[0]
    list_index += list_temp
    list_temp, pointeur = horizontal_bar(length, start_index)
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    pointeur -= length
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    return list_index

def digit_7(height, length, start_index, size):
    "write  digit 7"
    start_index += length
    list_index, pointeur = vertical_bar(height, start_index, size)
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    pointeur -= length
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    return list_index

def digit_8(height, length, start_index, size):
    "write  digit 8"
    list_index, pointeur = vertical_bar(height, start_index, size)
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    list_temp, pointeur = horizontal_bar(length, start_index)
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    list_temp = vertical_bar(height, pointeur, size)[0]
    list_index += list_temp
    return list_index

def digit_9(height, length, start_index, size):
    "write  digit 9"
    list_index, pointeur = horizontal_bar(length, start_index)
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    list_temp = vertical_bar(height, pointeur, size)[0]
    list_index += list_temp
    pointeur = pointeur - length
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    return list_index

def digit_0(height, length, start_index, size):
    "write  digit 0"
    list_index, pointeur = horizontal_bar(length, start_index)
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, start_index, size)
    list_index += list_temp
    list_temp, pointeur = vertical_bar(height, pointeur, size)
    list_index += list_temp
    list_temp = horizontal_bar(length, pointeur)[0]
    list_index += list_temp
    return list_index


def write_pi(approxpi, list_image, pointeur, height, length, size):
    "write numbers"
    list_index_finale = []
    dictionnary_fonction = {}
    dictionnary_fonction[0] = digit_0
    dictionnary_fonction[1] = digit_1
    dictionnary_fonction[2] = digit_2
    dictionnary_fonction[3] = digit_3
    dictionnary_fonction[4] = digit_4
    dictionnary_fonction[5] = digit_5
    dictionnary_fonction[6] = digit_6
    dictionnary_fonction[7] = digit_7
    dictionnary_fonction[8] = digit_8
    dictionnary_fonction[9] = digit_9

    for k in range(len(str(approxpi))):
        pointeur += length + 6
        if str(approxpi)[k] == ".":
            list_index_finale.append(pointeur + 3)
            list_index_finale.append(pointeur + 4)
            list_index_finale.append(pointeur + 3 - size)
            list_index_finale.append(pointeur + 4 - size)
            
        else:
            list_index_finale += dictionnary_fonction[int(str(approxpi)[k])](height,
             length, pointeur, size)

    for digit in list_index_finale:
        list_image[digit] = "Black"
    return list_image

def dictionnary_none(size):
    "creates a dictionary with coord in order and None in attribute"
    dictionnary = {}
    for j in range(size):
        for i in range(size):
            string = str(i) + "," + str(j)
            dictionnary[string] = None
    return dictionnary


def write_file(nom, size, list_image):
    "Write in the file the corresponding image according to the list"
    with open(nom, 'w', encoding='UTF-8') as fichier:
        fichier.write('P2\n')
        fichier.write(str(size))
        fichier.write(" ")
        fichier.write(str(size))
        fichier.write(" 10\n")
        for point in list_image:
            if point is None:
                fichier.write("8\n")    # Almost white is the color of the background
            if point is True:
                fichier.write("10\n")    # White when in circle
            elif point is False:
                fichier.write("5\n")    # Grey when out of circle
            elif point == "Black":
                fichier.write("0\n")    # Black


def generate_ppm_file(size, nb_points_tot, nb_float):
    " Generate a ppm file with the corresponding image"
    # conversion arbitrary unit to pixel
    list_image = size * size * [None]
    dictionnary_points = dictionnary_none(size)
    length = int(0.2*size/(nb_float+1))
    height = int(length*1.2)
    start = int((size/2)*size + size/3 +1)
    for repetition in range(0, 10):
        approxpi = approximate_pi.approximation(int(nb_points_tot/10)*(repetition+1))
        list_px = approximate_pi.list_approximation(int(nb_points_tot/10), size)
        approxpi = round(approxpi, nb_float)
        # creation of dictionary containing coordinate + color (all white to start)


        # We change the color for the points that are in the list_px
        for points in list_px:
            #0 abscissa, 1 ord
            dictionnary_points[str(points[0]) + "," + str(points[1])] = points[2]
        # Match the coordinates to the index on the image:
        for coord in dictionnary_points:
            x_abs, y_ord = int(str.split(coord, sep=",")[0]), int(str.split(coord, sep=",")[1])

            # inprint(f'Temps d\'exécution : {temps_exec:.2}ms')dexpx = int(y_ord*size + x+1)
            list_image[y_ord*size + x_abs] = dictionnary_points[coord]

        # Writing of pi
        list_image_digit = write_pi(approxpi, list_image, start, height, length, size)
        # Picture creation
        chaine = ""
        list_digit = [str(approxpi)[k] for k in range(1, len(str(approxpi)))]
        for k in range(1, len(list_digit)):
            chaine += list_digit[k]
        nom = f'img{repetition}_{str(approxpi)[0]}-{chaine}.ppm'
        write_file(nom, size, list_image_digit)


def creation_gif(les_images):
    "created a gif from the images"
    subprocess.call("convert -delay 50 " + les_images + " result.gif", shell=True)

def main():
    "main"
    #size of image output: argv[1], nbpoint: argv[2], nbfloat: argv[3], clean: argv[4]
    if len(sys.argv) != 4:
        print("Error, you need 3 arguments: size, nb_points, nb_float")
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
