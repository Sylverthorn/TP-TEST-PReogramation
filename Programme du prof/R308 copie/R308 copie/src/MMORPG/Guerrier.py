from mod import *
import json,pickle
class Guerrier(Personnage):
    """
    classe Guerrier: Hérite de Personnage.
    un Guerrier est un personnage avec une formation Martiale. Plus résistant et plus rapide, ses dégats sont plus importants
    un Guerrier n'a pas d'attribut spécifique à sa classe. Par contre les valeurs de ses attributs pointsDeVie et initiative sont calculés différement de ceux d'un personnage
    """
    def __init__(self,pseudo : str, niveau:int=1) :
        """
        la méthode d'initialisation de Guerrier fait appel en premier lieu à celle de Personnage (au travers de super())
        nous aurions pu aussi écrire Personnage.__init__(pseudo, niveau) qui aurait fait la même chose.
        :param pseudo: le pseudo du Guerrier
        :type pseudo : str
        :param niveau: le niveau de départ du Guerrier
        :type niveau: int
        """
        super().__init__(pseudo,niveau)

        self.points_de_vie = niveau*8+4
        self.initiative = niveau *4+6

    @Personnage.niveau.setter
    def niveau(self,niveau):
        """
        setter du niveau du Guerrier. ce setter surcharge celui de personnage car il modifie en même temps les points de vie et l'initiative du Guerrier avec ses propres régles de calcul
        :param niveau:
        :type niveau : int
        :return: None
        :exception TypeError: retourné si l'argument niveau n'est pas un entier
        """
        if isinstance(niveau,int):
            # appel au setter de personnage pour modifier le niveau. il est impossible d'appeler le setter par la méthode self.niveau (qui boucle) ni par super().niveau = niveau qui n'est pas interprété
            Personnage.niveau.fset(self,niveau)
            self.points_de_vie = niveau * 8 + 4
            self.initiative = niveau * 4 + 6

    def __str__(self):
        return f"Guerrier {super().__str__()} "
    def soin(self) -> None:
        """
        méthode de soin spécifique au Guerrier
        :return: None
        """
        self.points_de_vie = self.niveau*8+4

    def degats(self) -> int:
        """
        la méthode de dégats du Guerrier.

        :return: le nombre de points de dégats occasionnés
        :rtype: int
        """
        return self.niveau*2

    def toJson(self)-> str:
        """
        méthode de génération de la chaine Json pour le Guerrier

        :return: la chaine json
        :rtype: str
        """
        dict = {"class": "Guerrier", "pseudo": self.pseudo, "niveau": self.niveau, "points_de_vie": self.points_de_vie, "initiative": self.initiative}
        print(dict)
        return json.dumps(dict)

