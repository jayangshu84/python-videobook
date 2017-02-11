from math import pi


def liqvol(h, r = 10):
    v = (float(4*pi*r**3)/3) - float(pi*h**2*((3*r) - h)/3)
    return v

print liqvol(2)
