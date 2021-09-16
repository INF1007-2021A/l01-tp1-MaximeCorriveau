def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    position_initialev1 = 0
    position_initialev2 = 12
    v2_negatif = -v2


    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    while position_initialev1 != position_initialev2 :
        position_initialev1 +=  v1
        position_initialev2 += v2_negatif


    positionRencontre = position_initialev1


    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
