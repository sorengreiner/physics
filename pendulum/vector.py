import math

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Print(self):
        print("{0},{1}".format(self.x, self.y))

    def Length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def SqrLength(self):
        return self.x*self.x + self.y*self.y

    def Normalize(self):
        length = self.Length()
        return self.Mul(1.0/length)

    def Mul(self, s):
        return Vector2d(self.x*s, self.y*s)

def Add(u, v):
    return Vector2d(u.x + v.x, u.y + v.y)

def Sub(u, v):
    return Vector2d(u.x - v.x, u.y - v.y)


def Dot(u, v):
    return u.x*v.x + u.y*v.y


    