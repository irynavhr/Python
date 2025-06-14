
import math
def factors(x):
    t = tuple()
    for i in range(1,x+1):
        if x % i == 0:
            t += (i,)
    return t

def gcd(x, y):
    tx = factors(x)
    ty = factors(y)
    set_factors = set()
    for i in tx:
        if i in ty:
            set_factors.add(i)
    return max(set_factors)

print(gcd(165, 15235))