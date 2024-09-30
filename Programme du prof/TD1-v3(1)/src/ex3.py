"""
module de découverte de la documentation à partir de la docstring
"""
import json
import pickle

def affiche(texte:str)->str:
    """
    fonction qui renvoie la chaine passée précédée d'une introduction

    :param texte: chaine de caractère à afficher
    :type texte: str
    :return: la chaine de cararctère agrémentée
    :rtype: str
    """

    return f"chaine à afficher : {texte}"

class Velo:
    """
    classe vélo:

    cette classe permet de définir un Vélo possédant une couleur, une taille de roue en pouce, un nombre de vitesse et une marque

    .. py:attribute:: marque:

        marque du vélo

        :type: str

    .. py:attribute:: couleur:

        couleur du vélo

        :type: str

    .. py:attribute:: taillePneu

        taille du pneu en pouces

        :type: int

    .. py:attribute:: nbVitesses

        nombre de vitesse du vélo

        :type: int
    """

    def __init__(self,marque : str, couleur : str, taillePneu: int, nbVitesses:int):
        self.couleur = couleur
        self.marque = marque
        self.taillePneu = taillePneu
        self.nbVitesses = nbVitesses
        self.vitesse_courante = 0


    def __str__(self) -> str:
        return f"Vélo de marque {self.marque} de couleur {self.couleur} " \
               f"avec des pneus de taille {self.taillePneu} pouces et {self.nbVitesses} vitesses"

    def gear_up(self, vitesse:int =1) -> int :
        """
        fonction permettant d'accélerer

        :param vitesse: nb de vitesse passée
        :type vitesse: int
        :return: vitesse courante
        :rtype: int
        """
        if self.vitesse_courante <= self.nbVitesses-vitesse:
            self.vitesse_courante += vitesse
        else:
            raise OverflowError("vitesse maximum atteinte")
        return self.vitesse_courante

    def gear_down(self, vitesse:int =1) -> int :
        """
        fonction permettant de déceler

        :param vitesse: nb de vitesse descendue
        :type vitesse: int
        :return: vitesse courante
        :rtype: int
        """
        if self.vitesse_courante >- vitesse:
            self.vitesse_courante -= vitesse
        else:
            raise OverflowError("vitesse minimale atteinte")
        return self.vitesse_courante

if __name__=="__main__":
    chaine = input("saisir du texte à afficher: ")
    print (affiche(chaine))
    velo1 = Velo("peugeot","bleu",28,21)
    print (velo1)
    for i in range(12):
        print (f" j'accélere :  vitesse {velo1.gear_up()}")
    for i in range(8):
        print(f" je freine :  vitesse {velo1.gear_down()}")
    print(f"j'accélere {velo1.gear_up(4)}")
    print(f"je ralenti  {velo1.gear_down(8)}")
    print(velo1.__dict__)
    with open("test.txt","w") as f:
        print(json.dump(velo1.__dict__,f))

    with open ("test.txt","r") as f2:
        res = json.load(f2)
        print(f"dicionnaire issu de json {res}")
        velo3 = Velo(res["marque"],res["couleur"],res["taillePneu"],res["nbVitesses"])
        print(f"velo3 Json {velo3}")

    with open("data.bin","wb") as fb:
        pickle.dump(velo1,fb)

    with open("data.bin","rb") as fb2:
        velo4 = pickle.load(fb2)
        print (f"velo4 pickle {velo4}")
        velo4.gear_up()
        print(velo4)