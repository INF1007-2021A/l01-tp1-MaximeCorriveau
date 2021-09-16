import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    vitesseInitiale_en_mètre_par_seconde = vitesseInitiale *1000/3600
    vitesseFinale_en_mètre_par_seconde = vitesseFinale * 1000/3600
    accélération = (vitesseFinale_en_mètre_par_seconde - vitesseInitiale_en_mètre_par_seconde) / duree

    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = (vitesseInitiale_en_mètre_par_seconde * duree + 1/2 * accélération * duree **2) + positionInitiale

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
