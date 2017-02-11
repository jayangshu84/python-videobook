def accelaration(v1, v2, t1, t2):
    a = float(v2 - v1) / float(t2 - t1)
    return a

print accelaration(0, 10, 0, 20)
