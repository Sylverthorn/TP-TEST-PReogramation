import math
from typing import Union

class Point:
    """
    classe définissant un point dans un référentiel cartésien à deux dimensions

    .. py:attribute:: x:

        abscisse du point

        :type: float

    .. py:attribute:: y:

        ordonnée du point

        :type: float
    """
    def __init__(self,x:float=0,y:float=0):
        self.__x :float = x
        self.__y :float = y

    def __str__(self) ->str:
        return f"Point x: {self.__x} y: {self.__y}"

    @property
    def x(self) -> float:
        """
        getter de l'asbcisse x

        :return: valeur de x


        """
        return self.__x
    @x.setter
    def x(self,x:Union[float,int]):
        """
        setter de l'abscisse x

        :param x: valeur pour l'abscisse
        :raise TypeError: erreur générée si la valeur fournie n'est pas un entier ou un réel
        """
        if isinstance(x,Union[float,int]):
            self.__x = x
        else:
            raise TypeError("la valeur fournie n'est pas du type int ou float")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        """
            setter de l'abscisse x

            :param x: valeur pour l'abscisse
            :raise TypeError: erreur générée si la valeur fournie n'est pas un entier ou un réel
            """
        if isinstance(y,Union[float,int]):
            self.__y = y
        else:
            raise TypeError("la valeur fournie n'est pas du type int ou float")
    def distance_coordonnees(self,x:float=0,y:float=0)->float:
        """
        fonction de calcul de la distance entre le point courant
        et une autre position dont on a les coordonnées

        :param x: abscisse de l'autre point
        :type x: float
        :param y: coordonnées de l'autre point
        :type y: float
        :return: la distance calculée
        :rtype: float
        """
        res = math.sqrt((self.__x-x)*(self.__x-x) + (self.__y-y)*(self.__y-y))
        return res

    def distance_point(self,camarade: 'Point') -> float:
        """
                fonction de calcul de la distance entre le point courant
                et un autre point

                :param camarade: l'autre point
                :type camarade: Point
                :return: la distance calculée
                :rtype: float
                """
        res = math.sqrt((self.__x-camarade.__x)*(self.__x-camarade.__x) + (self.__y-camarade.__y)*(self.__y-camarade.__y))
        return res

    def __eq__(self, other : 'Point'):
        if self.__x == other.__x and self.__y == other.__y:
            return True
        else:
            return False
