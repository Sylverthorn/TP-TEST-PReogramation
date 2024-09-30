"""
définition de la classe Tasse de l'exercice 2
"""

class Tasse:
    """
    Classe définissant une tasse.

    .. py:attribute:: matiere:

        matière de la tasse, attribut de classe

    .. py:attribute:: couleur:

        couleur de la tasse, attribut d'instance

    .. py:attribute:: contenance:

        contenance de la tasse, attribut d'instance

    .. py:attribute:: marque:

        marque de la tasse, attribut d'instance.
    """

    matiere:str  = "ceramique"

    def __init__(self,couleur:str, contenance:int, marque:str):
        """
        méthode d'instanciation d'une tasse

        :param couleur: couleur de la tasse
        :type couleur: str
        :param contenance: contenance de la tasse en ml
        :type contenance: int
        :param marque: marque de la tasse
        :type marque: str
        """
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self) -> str:
        return f"tasse de matière {self.matiere} de couleur {self.couleur} " \
               f"contenant {self.contenance} ml et de marque {self.marque}"

    def ajout(self,contenu) -> None:
        """
        méthode d'ajout d'un contenu comme attribut d'isntance à l'objet courant
        :param contenu: le contenu de la tasse
        :type contenu: str
        """
        self.contenu = contenu

    def bue(self) -> str:
        """
        méthode qui efface l'attribut contenu

        :return: renvoie un rappel de la boisson bue aprés effacement
        """
        chaine=f"boisson {self.contenu} bue"
        del(self.contenu)
        return chaine

if __name__=="__main__":
    t1 = Tasse("bleue",250,"tefal")
    print(t1)
    t1.ajout("chocolat")
    print (t1.contenu)
    print(vars(t1))
    t1.bue()
    print(vars(t1))