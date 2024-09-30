import math
import pytest

from R308.src.Formes.Cercle import Cercle
from R308.src.Formes.Point import Point
c1 = Cercle (2)
def test_diametre():

    assert c1.diametre() == 4

def test_perimetre():
    assert c1.perimetre() == math.pi * 2 * 2

def test_contient():
    p = Point(5,6)
    assert c1.contient(p) == False

def test_contient2():
    p = Point(1,1)
    assert c1.contient(p) == True

def test_creation_cercle():
    with pytest.raises(TypeError):
        Cercle("toto")

def test_intersection():
    c2 = Cercle(2,Point(1,1))
    assert c1.intersection(c2) == True

def test_intersection2():
    c3 = Cercle(1,Point(5,4))
    assert c1.intersection(c3) == False