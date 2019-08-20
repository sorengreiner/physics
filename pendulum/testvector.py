from vector import *

a = Vector2d(3,4)
b = Vector2d(10,2)

a.Print()
b.Print()

c = Add(a,b)
c.Print()

d = Dot(a,b)
print("{}".format(d))

l = a.Length()
print("{}".format(l))

sl = a.SqrLength()
print("{}".format(sl))

m = a.Mul(3.5)
m.Print()


# Test swinging pendulum
force_g = Vector2d(0, -9.82)

origo = Vector2d(0, 0)
ball = Vector2d(0,-1)

s = Sub(origo, ball)

force_s = s.Mul( -Dot(force_g, s)/s.SqrLength() )

force_s.Print()

force = Add(force_s, force_g)
force.Print()

