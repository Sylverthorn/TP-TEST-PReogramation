import sys

from mod import *
from Joueur import Joueur

def main():
    p : Personnage = Personnage("Merlin")
    print(p)
    p2 : Personnage = Personnage("Conawn",45)
    print(p2)
    p3 : Personnage = Personnage("Merlin")
    g3 : Guerrier = Guerrier ("Merlin")
    print(g3)
    g3.niveau = 10
    print (g3)
    try:
        niveau = input("saisir le niveau du personnage toto")
        g4 = Personnage("toto",niveau)
    except TypeError as tr:
        print(tr)
    else:
        print(g4)
        
    if g3 == p:
        print("les personnages p et p3 sont identiques")
    else :
        print("les personnages p et p3 sont différents")

    p.combat(p2)

    print(p)

    print(p2)
    if (p.points_de_vie>0):
        print(f"le personnage {p.pseudo} a vaincu {p2.pseudo}")
    elif (p2.points_de_vie>0):
        print(f"le personnage {p2.pseudo} a vaincu {p.pseudo}")
    else:
        print(f"les personnages {p2.pseudo} et {p.pseudo} se sont entretués")

    p.soins()
    p2.soins()
    print(p)
    print(p2)

    g1 : Guerrier = Guerrier("arnauld",10)
    print (g1)

    g3 : Guerrier = Guerrier("Merlin")
    if p3 == p:
        print("les personnages p et p3 sont identiques")
    else:
        print("les personnages p et p3 sont différents")

    m1 : Mage = Mage("toto", 12)
    print(m1)
    m1.combat(g1)
    if (m1.points_de_vie>0):
        print(f"le personnage {m1.pseudo} a vaincu {g1.pseudo}")
    elif (g1.points_de_vie>0):
        print(f"le personnage {g1.pseudo} a vaincu {m1.pseudo}")
    else:
        print(f"les personnages {g1.pseudo} et {m1.pseudo} se sont entretués")

    chaine = p2.toJson()
    print(chaine)
    p4 = fromJson(chaine)
    print(p4)
    chaine = g1.toJson()
    p4 = fromJson(chaine)
    print(p4)
    print("serialisation \n")
    buff = p4.toBuffer()
    p5 = Personnage.fromPickle(buff)
    print(p5)

    j1 : Joueur = Joueur("arnauld", 7)
    j1.ajout_joueur(p)
    print(j1)

    liste=[p,p2,p,p4]
    j2 : Joueur = Joueur("toto",liste=liste)
    print(j2)

    pp = j1.cherche_id(4)
    if pp is None:
        print(f"le joueur {j1.nom} ne posséde pas de 4éme personnage")
    else:
        print(pp)

    pp = j1.cherche_nom("merlin")
    if pp is None :
        print(f"le joueur {j1.nom} ne posséde pas le personnage nommé merlin")
    else:
        print(pp)

    pp = j2.cherche_personnage(p3)
    if pp is None:
        print(f"le joueur {j2.nom} ne posséde pas le personnage nommé merlin")
    else:
        print(f"le joueur {j2.nom} posséde le personnage {pp}")

    print(j2)
    j2.delete_id(0)
    print(j2)

    
    print ("ecriture pickle")
    with open("data.bin", "wb") as fichier:
        pickle.dump(j2,fichier)

    print("lecture pickle")
    with open("data.bin", "rb") as fichier:
        j = pickle.load(fichier)
        print (f"data obtenu {j}")


    #print (f"type {type('bonjour')}")
    """    
    chaine = pickle.dumps(j2)
    j5 = pickle.loads(chaine)
    print (j5)
    """

if __name__ == "__main__":
    sys.exit(main())