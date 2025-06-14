import math
def f(func, a, b = None):
    if b == None:
        return func(a)
    return func(a, b)
print(f(math.sqrt, 36))
print(f(math.pow, 3, 3))