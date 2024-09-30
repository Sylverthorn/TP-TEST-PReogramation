import sys,os
sys.path.append(os.path.join(__file__,"../"))
import Point
import Cercle


def main():
    p1 = Point.Point()
    print(p1.__dict__)
    print(f"distance {p1.distance_coordonnees(4,3)}")
    p2 = Point.Point(2, 4)
    print(f"distance Point {p1.distance_point(p2)}")

    c1 = Cercle.Cercle(5)
    print (c1)
    c2 = Cercle.Cercle(8,p2)
    print(c2)


    print(f" cercle c1 de diametre {c1.diametre()} de périmetre {c1.perimetre():.1f} et de surface {c1.surface():.1f}")
    print(f" cercle c2 de diametre {c2.diametre()} de périmetre {c2.perimetre():.1f} et de surface {c2.surface():.1f}")
    if (c1.intersection(c2)):
        print ("les cercles c1 et c2 sont en intersection")
    else:
        print("les cercles ne sont pas en intersection")

if __name__ == "__main__":
    sys.exit(main())
