import math

from R308.src.Formes.Point import Point
def test_distance_coordonnee():
    p1 = Point(2,3)
    assert p1.distance_coordonnees(2,3) == 0

def test_distance_point():
    p1 = Point(2,3)
    p2 = Point(0,0)
    assert p1.distance_point(p2) == math.sqrt(4+9)

