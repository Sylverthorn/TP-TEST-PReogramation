#import sys,os
#sys.path.append(os.path.join(__file__,"../"))
from Personnage import Personnage
from Guerrier import Guerrier
from Mage import Mage

import json, pickle

def fromJson( chaine: str):
    """
    méthode pour créer un Personnage (typé) en fonction de la lecture de la chaine Json
    :param chaine: la chaine lue
    :type chaine: str
    :return: le Personnage
    :rtype: Union[Personnage, Guerrier, Mage]
    """
    dict = json.loads(chaine)
    if dict["class"] == "Personnage":
        p: Personnage = Personnage(dict["pseudo"], dict["niveau"])
    elif dict["class"] == "Guerrier":
        p: Guerrier = Guerrier(dict["pseudo"], dict["niveau"])
    elif dict["class"] == "Mage":
        p: Mage = Mage(dict["pseudo"], dict["niveau"])
        p.mana = dict["mana"]
    p.points_de_vie = dict["points_de_vie"]
    p.initiative = dict["initiative"]
    return p

