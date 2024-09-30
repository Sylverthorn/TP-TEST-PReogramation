from Personnage import Personnage
from typing import List

class Joueur:
    """
    classe Joueur: décrit une joueur de Jeu de Rôle. il posséde un ensemble de personnage

    .. py:attribute:: nom

        Nom du joueur.

        :type: str

    .. py:attribute:: maximum

        nombre maximum que personnage que le joueur peut posséder

        :type: int

    .. py:attribute:: liste

        la liste des personnages d'un joueur

        :type: List[Personnage]

    """
    def __init__(self, nom :str, maximum: int = 5, liste: List[Personnage] = []):
        """
        initialise un joueur

        :param nom: nom du joueur
        :param maximum: nombre maximum de personnage pour le joueur
        :param liste: la liste des personnages

        """
        self.__nom = nom
        self.__maximum = maximum
        if len(liste) <= maximum:
            self.__liste = liste
        else:
            self.__liste = liste[:self.__maximum]

    def __str__(self):
        rep = f"Joueur {self.__nom} possédant {len(self.__liste)} Personnage(s):"
        if len(self.__liste)>0:
            for p in self.__liste:
                rep += f"\n - {p}"
        return rep

    def ajout_joueur(self, p:Personnage) ->bool:
        """
        méthode permettant d'aajouter un personnage à la liste
        :param p: le personnage à ajouter
        :return: True si on peux l'ajouter, False sinon

        """
        if len(self.__liste) < self.__maximum:
            self.__liste.append(p)
            return True
        else:
            return False

    def cherche_id(self,index : int) -> Personnage:
        """
        méthode permettant de renvoyer le personnage dont la position est passée en argument.
        :param index: la position dans la liste
        :return: le Personnage si il y en a un à l'index donné ou None.
        """
        if 0 <= index < self.__maximum:
            if index <= len(self.__liste):
                return self.__liste[index]
        return None

    def cherche_nom(self, nom:str) -> Personnage:
        """
        recherche d'un personnage dans la liste en utilisant le nom du personnage.

        :param nom: Nom de personnage recherché
        :return: le Personnage ou None si non trouvé
        """
        for p in self.__liste:
            print(f"liste : {p}")
            if p.pseudo == nom:
                return p
        return None

    def cherche_personnage(self, p :Personnage) -> Personnage:
        """
        recherche d'un personnage dans la liste en utilisant le personnage.

        :param p: Le personnage recherché
        :return: le Personnage ou None si non trouvé
        """
        for per in self.__liste:
            if per == p:
                return per
        return None

    def delete_id(self,index : int) -> bool:
        """
        méthode permettant de supprimer un personnage de la liste du joueur à l'aide de son numéro

        :param index: le numéro du personnage dans la liste du joueur

        :type index: int

        :return: True si l'index est dans la liste et correspond à un joueur, False sinon

        :rtype : bool
        """

        if 0<= index < len(self.__liste):
            self.__liste.pop(index)
            #del(self.__liste[index])
            return True
        return False

    def delete_nom(self, nom:str) -> bool:
        """
        méthode permettant de supprimer un personnage de la liste du joueur à l'aide de son nom

        :param nom: le nom du personnage à chercher dans la liste du joueur

        :type nom: str

        :return: True s'il y a un personnage portant le nom passé dans la liste, False sinon

        :rtype : bool

        """
        for i in range(len(self.__liste)):
            if self.__liste[i].pseudo == nom:
                self.__liste.remove(self.__liste[i])
                # del(self.__liste[i])
                return True
        return False

    def delete_personnage(self, per: str) -> bool:
        """
            méthode permettant de supprimer un personnage de la liste du joueur à l'aide du personnage directement

               :param per: le nom du personnage à chercher dans la liste du joueur

               :type per: Personnage

               :return: True s'il y a un personnage identique au personnage passé en argument, False sinon

               :rtype : bool

               """
        for p in self.__liste:
            if p == per:
                self.__liste.remove(p)
                # del(p)
                return True
        return False


    @property
    def nom(self) ->str:
        return self.__nom