import pytest

from R308.src.Formes.Rectangle import Rectangle
from R308.src.Formes.Point import Point

point = Point(2,4)
point2= Point(3,6)

def test_creation_rectangle():
    """
    test du retour d'exception si le premier argument, la longueur n'est pas entier ou un réel
    :return: None
    """
    with pytest.raises(TypeError):
        Rectangle("toto",0)

def test_surface():
    r1= Rectangle(2,4,point)
    assert r1.surface() == 8

def test_perimetre():
    r1 = Rectangle(2, 4, point)
    assert r1.perimetre() == 12

def test_contient():
    r1 = Rectangle(2, 4, point)
    p1 = Point(2.5,6)
    assert r1.contient(p1)
def test_contient2():
    r1 = Rectangle(2, 4, point)
    p1 = Point(2.5,3)
    assert r1.contient(p1) == False

def test_point_bas_gauche():
    r1 = Rectangle(2, 4, Point(2,4))
    assert r1.pointBasGauche() == point

def test_point_haut_droit():
    r1 = Rectangle(2, 4, point)
    p2 = Point(4,8)
    assert r1.pointHautDroit() == p2

def test_point_haut_gauche():
    r1 = Rectangle(2, 4, point)
    p2 = Point(2,8)
    assert r1.pointHautGauche() == p2

def test_point_bas_droit():
    r1 = Rectangle(2, 4, point)
    p2 = Point(4,4)
    assert r1.pointBasDroit() == p2
