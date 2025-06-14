def argmax(*l):
    m = max(l)
    return m, l.index(m)
t = (5, -2, 695, 83, -99, 123, 15, -55)
print(argmax(*t))