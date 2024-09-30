import pickle
from io import BytesIO

class data:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x = {self.x} y = {self.y}"

def main():
    d = data(1,2)
    print(d.__dict__)
    with open('data.txt', 'wb') as f:
        print ("ouverture fichier ecriture")
        pickle.dump(d,f)
        f.closed
    with open('data.txt', 'rb') as f2:
        print("ouverture fichier lecture")
        d2 = pickle.load(f2)
        print(f"{d2.__class__} {d2.__dict__}")
        f2.closed

"""    buffer = BytesIO()
    pickle.dump(d,buffer)
    seq = buffer.getvalue()
    buffer2 = BytesIO(seq)
    d2 = pickle.load(buffer2)
    print(d2)
"""


main()
