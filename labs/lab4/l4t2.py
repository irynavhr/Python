import math
import random as rnd
x3 = []
for _ in range(20):
    x3.append(((((rnd.randrange(1,10)*10 + 0)*10 + rnd.randrange(1,10))*10 + 0)*10 + rnd.randrange(1,10))/100000)
print(f'x3 = {x3}')
