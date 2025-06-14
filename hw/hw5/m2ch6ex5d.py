import math
def factors(x):
    t = tuple()
    for i in range(1,x+1):
        if x % i == 0:
            t += (i,)
    return t

print(factors(20))
