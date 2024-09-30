import math
import sys,os
sys.path.append(os.path.join(__file__,"../"))
from . import Point

class Cercle:
    """
    classe Cercle : définit un cercle dans un repére cartésien à deux dimensions

    .. py:attribute:: rayon:

        rayon du cercle

        :type: float

    .. py:attribute:: centre:

        point centre du cercle

        :type: Point
    """

    def __init__(self,rayon : float, centre : 'Point' = None):
        """
            constructeur de Cercle

        :param rayon: valeur affectée au rayon
        :type rayon: float ou int
        :param centre: Le Point centre utilisé (objet de la classe Point). La
            valeur par défaut est None (
        :type centre: Point, or None
        """
        if isinstance(rayon,(int,float)):
            self.__rayon = rayon
        else :
            raise TypeError("Le rayon doit être un entier ou un réel")
        if centre is not None:
            self.__centre = centre
        else:
            self.__centre = Point.Point(0,0)


    def __str__(self):
        return f"Cercle de centre {self.__centre} et de rayon {self.__rayon}"

    def diametre(self) -> float:
        """
        fonction déterminant le diamétre du cercle

        :return: la valeur du diamètre
        :rtype: float
        """
        return 2*self.__rayon

    def perimetre(self) -> float:
        """
        fonction déterminant le périmétre du cercle

        :return: la valeur du périmètre
        :rtype: float
        """
        return self.diametre()*math.pi

    def surface(self) -> float:
        """
        fonction déterminant la surface du cercle

        :return: la valeur de la surface
        :rtype: float
        """
        return self.__rayon*self.__rayon*math.pi

    def intersection(self,autrecercle : 'Cercle') ->bool:
        """
        fonction permettant d'indiquer si deux cercles voient leur perimètre se couper

        :param autrecercle: l'autre cercle
        :type autrecercle: Cercle
        :return: Vrai si c'est les deux périmétre se croisent, Faux sinon
        :rtype: bool
        """
        if (self.__centre.distance_point(autrecercle.__centre))< self.__rayon+autrecercle.__rayon :
            return True
        else:
            return False

    def contient(self,p:'Point') ->bool:
        """
        fonction indiquant si un point se trouve dans la surface du cercle

        :param p: le point à tester
        :type p: Point
        :return: Vari si le point est contenu dans la surface, Faux sinon
        :rtype: bool
        """
        if self.__centre.distance_point(p) < self.__rayon:
            return True
        else:
            return False