"""
module de la classe Rectangle
"""
from R308.src.Formes.Point import Point
class Rectangle:
    """
    classe définissant un rectangle dans un répére cartésien à deux dimensions

    .. py:attribute:: longueur

        la longueur du rectangle. Elle est définie comme étant paralléle à l'axe des abscisses

        :type:float

    .. py:attribute:: hauteur

        la hauteur du rectangle. Elle est définie comme étant parallèle à l'axe des ordonnées

        :type: float

    .. py:attribute:: pointBasGauche

        le point situé en bas à gauche du rectangle.

        :type: Point
    """

    def __init__(self,longueur: float = 1,hauteur:float = 1, pointBasGauche: 'Point' = Point(0,0), pointHautDroit: 'Point' = None):
        if not isinstance(longueur,(float,int)) or not isinstance(hauteur,(float,int)):
            raise TypeError("la longueur ou la largeur ne sont pas dans le bon type réel ou entier")
        self.__pointBasGauche = pointBasGauche
        if pointHautDroit is not None:
            if pointHautDroit.x < pointBasGauche.x :
                x1 = pointHautDroit.x
                x2 = pointBasGauche.x
            else :
                x2 = pointHautDroit.x
                x1 = pointBasGauche.x
            if pointHautDroit.y < pointBasGauche.y :
                y1 = pointHautDroit.y
                y2 = pointBasGauche.y
            else :
                y2 = pointHautDroit.y
                y1 = pointBasGauche.y

            self.__pointBasGauche = Point(x1,x2)
            self.__longeur = x2-x1
            self.__hauteur = y2-y1
        else:
            self.__longeur = longueur
            self.__hauteur = hauteur
    def surface(self) -> float:
        """
        méthode retournant la surface du rectangle

        :return: valeur de la surface
        :rtype: float
        """
        return self.__hauteur*self.__longeur

    def perimetre(self) -> float:
        """
        méthode déterinant le péerimétre du rectangle

        :return: valeur du périmètre
        :rtype: float
        """
        return (self.__hauteur+self.__longeur)*2

    def contient(self,p:'Point') -> bool:
        """
        fonction déterminant si un point appartient à la surface du rectangle

        :param p: le point à tester
        :return: Vrai si le point est sur la surface, Faux sinon
        :rtype: bool
        """
        res = False
        if  self.__pointBasGauche.x < p.x < self.__pointBasGauche.x + self.__longeur and  \
            self.__pointBasGauche.y < p.y < self.__pointBasGauche.y + self.__hauteur:
            res = True
        return res

    def pointBasGauche(self):
        return self.__pointBasGauche

    def pointHautGauche(self):
        p = Point(self.__pointBasGauche.x,self.__pointBasGauche.y+self.__hauteur)
        return p

    def pointHautDroit(self):
        p = Point(self.__pointBasGauche.x+self.__longeur, self.__pointBasGauche.y + self.__hauteur)
        return p

    def pointBasDroit(self):
        p = Point(self.__pointBasGauche.x+self.__longeur, self.__pointBasGauche.y)
        return p
