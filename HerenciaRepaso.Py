class X:
    def __init__(self,A,B) :
        self.A = A
        self.B = B

    def sumar (self) :
        return F"la suma es : {self.A + self.B}"

class Y(X):
    def __init__(self, A, B,C):
        super().__init__(A,B)
        self.C = C

xy1 = Y (2,3,4)

print (xy1.sumar())