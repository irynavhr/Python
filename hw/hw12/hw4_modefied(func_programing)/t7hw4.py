# modified by Iryna Hrytsenko

import random
from functools import reduce

n = random.randint(5, 15)
print("n = ", n)
list_a = tuple(round((random.random()*20)-10, 2) for i in range(n))
print(list_a)

double_sum = reduce(lambda a, b: a+b, list_a)*2

print(f"duobled sum = {double_sum}")