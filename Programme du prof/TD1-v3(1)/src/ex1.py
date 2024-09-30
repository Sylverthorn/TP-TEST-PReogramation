"""
module de test des différents types d'arguments pour les fonctions python
"""

from typing import Any

def max(a:int, b:int)-> int:
    """
    fonction retournant le max de deux nombres

    :param a: première valeur
    :type a: int
    :param b: 2ème valeur
    :type b: int
    :return: le maximum des deux valeurs
    :rtype: int
    """
    if a > b :
        return a
    return b

def max2(a:int, seuil:int = 10) -> bool:
    """
    fonction max2, renvoie si une valeur est supérieure à un seuil

    :param a: valeur
    :type a: int
    :param seuil: seuil fixé par défaut à 10
    :type seuil: int
    :return: Vrai si a est supérieur au seuil, Faux sinon
    :rtype: boolean
    """
    if a > seuil :
        return True
    return False

def maxListe(*args:Any) -> int:
    """
    fonction maxListe, trouve le maximum de l'ensemble de valeurs fournies en argument

    :param args: valeur
    :type args: int | float
    :return: maximum de la liste
    :rtype: int | float
    """
    max = args[0]
    for p in args:
        if p > max:
            max = p
    return max

def maxListeSeuil(seuil: int, *args: Any) -> int:
    """
    fonction maxListeSeuil, trouve le nombre de valeurs de l'ensemble de valeurs fournies en argument supérieures à un seuil donné

    :param seuil: seuil à dépasser
    :type seuil: int
    :param args: valeur
    :type args: int | float
    :return: maximum de la liste
    :rtype: int
    """
    nb = 0
    for p in args:
        if p > seuil:
           nb+=1
    return nb

def listedico(**kwargs):
    """
    fonction listDico, affiche l'ensemble des arguments nommés non défini

    :param kwargs: liste des arguments nommés
    """
    for key, value in kwargs.items():
        print("\n liste des paires du dictionnaires: \n")
        print(f"{key}:{value}")

if __name__ == "__main__":
    print(f"maximum 2 nombres (2,12): {max(2,12)}")
    print(f"supérieur au seuil défaut {max2(12)}")
    print(f"supérieur au seuil  : {max2(12,2)}")
    print(f"max liste : {maxListe(23,3,5,17,2,20,3,78,3,45)}")
    print(f"nb max seuil : {maxListeSeuil(23, 3, 5, 17, 2, 20, 3, 78, 3, 45)}")

    listedico(salut="bonjour",taille=12.3,chaine="c'est le jour",jour=23)