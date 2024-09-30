
import json, pickle

class Personnage():
    """
    Classe définissant un personnage. C'est le squelette de base de l'ensemble des classes de personnages (Guerrier et Mage).
    Elle définit les méthodes de combat et attaque qui sont communes à tous les personnages quelle que soient leur type

    .. py:attribute:: pseudo

        le nom du personnage

        :type: str

    .. py:attribute:: niveau

        définit le niveau du personnage. Caractéristique donnant l'expérience dy personnage et intervenant dans les calculs de l'initiative et des points de vie

        :type: int

    .. py:attribute:: initiative

        capacité de réaction du personnage. determine l'ordre d'attaque lors d'un combat

        :type: int

    .. py:attribute:: pointsDeVie

        nombre de points de vie du personnage

        :type: int
    .. py:exception:: TypeError:

        Si le niveau fourni n'est pas un entier, une exeception Type Error est levée
    """
    def __init__(self, pseudo : str, niveau : int =1):
        """
        constructeur de Personnage

        :param pseudo: pseudo du personnage
        :type pseudo : str
        :param niveau: le niveau du personnage crée. Par défaut le personnage est de niveau 1
        :type niveau: int
        """
        self.__pseudo = pseudo
        if isinstance(niveau, int):
            self.__niveau = niveau
            self.__points_de_vie = niveau
            self.__initiative = niveau
        else:
            raise TypeError("le niveau doit être de type entier")

    def __str__(self) -> str:
        return f"{self.__pseudo} est de niveau {self.__niveau} possède {self.__points_de_vie} " \
               f"points de vie et une initiative de {self.__initiative}"

    def degats(self) -> int:
        """
        méthode permettant de générer les dégats. Introduite afin de prendre en compte les dégats différents suivant la classe de personnage et l'heritage

        :return: le nombre de points de dégats de l'attaque
        :rtype: int
        """
        return self.__niveau

    def attaque(self, opposant):
        """
        méthode permettant de gérer un échange de coup. Cette méthode pourrait être privée car uniquement utilisée par la méthode combat

        :param opposant: c'est le personnage attaqué par le personnage courant
        :return: None
        """
        if (self.__initiative>opposant.__initiative):
            opposant.__points_de_vie -= self.degats()
            if opposant.__points_de_vie < 0:
                self.__points_de_vie -= opposant.degats()
        elif (opposant.__initiative>self.__initiative):
            self.__points_de_vie -= opposant.degats()
            if self.points_de_vie < 0:
                opposant.__points_de_vie -= self.degats()
        else:
            opposant._points_de_vie -= self.degats()
            self.__points_de_vie -= opposant.degats()

    def combat(self,opposant):
        """
        méthode gérant un combat aboutissant à la mort d'au moins un personnage.

        :param opposant: c'est le personnage attaqué par le personnage courant
        :return: None
        """
        while (self.__points_de_vie>0 and opposant.__points_de_vie>0) :
            self.attaque(opposant)

    def soins(self):
        """
        méthode permettant de soigner un personnage, c'est à dire de lui remettre ses points de vie à leur valeur initiale
        :return: None
        """
        self.__points_de_vie = self.__niveau

    def __eq__(self,other):
        """
        méthode permettant de comparer si deux personnages sont les mêmes. La comparaison s'effectue sur le pseudo et le niveau
        cette methode est appelée de façon implicite par le ==

        :param other: Le personnage à comparer au personnage courant
        :return: True si les deux personnages sont identiques, False sinon
        """
        if self.__pseudo == other.__pseudo and self.__niveau == other.__niveau and type(self) == type(other):
            return True
        else:
            return False

    @property
    def points_de_vie(self) -> int:
        return self.__points_de_vie

    @points_de_vie.setter
    def points_de_vie(self,pv):
        if pv > 0:
            self.__points_de_vie = pv

    @property
    def initiative(self) -> int:
        return self.__initiative

    @initiative.setter
    def initiative(self, initiative:int):
        if isinstance(initiative, int):
            if initiative > 0:
                self.__initiative = initiative
            else:
                raise ValueError("l'initiative doit être positive")
        else:
            raise TypeError("l'initiative doit être un entier")


    @property
    def pseudo(self) -> str:
        return self.__pseudo

    @property
    def niveau(self) -> int:
        return self.__niveau

    @niveau.setter
    def niveau(self, niveau: int):
        """
        accesseur setter pour le niveau. modifie aussi les points de vie et l'initiative

        :param niveau: le niveau
        :type niveau: int
        :raise TypeError: si le niveau passé n'est pas un entier, cette exception est levée
        :raise ValueError: si le niveau est négatif, cette exception est levée
        """
        if isinstance(niveau,int):
            if niveau >= 0:
                self.__niveau = niveau
                self.__initiative = niveau
                self.__points_de_vie = niveau
            else:
                raise ValueError("le niveau doit être positif")
        else :
            raise TypeError("le niveau doit être un entier")

    def toJson(self) -> str:
        """
        méthode générant une chaine Json décrivant le personnage
        :return:
        """
        dict = {"class" : "Personnage" , "pseudo": self.__pseudo, "niveau": self.__niveau, "points_de_vie" : self.__points_de_vie, "initiative" : self.__initiative}
        return json.dumps(dict)

    def toBuffer(self) -> bytes:
        """
        génére un binaire du personnage

        :return: le flux binaire

        :rtype : bytes

        """
        ser = pickle.dumps(self)
        return ser
    @staticmethod
    def fromPickle(buffer) -> object:
        """
        permet à partir d'un binaire de récupérer un personnage

        :param buffer: la chaine binaire

        :return: l'objet récupéré (le personnage)

        """
        object = pickle.loads(buffer)
        return object

