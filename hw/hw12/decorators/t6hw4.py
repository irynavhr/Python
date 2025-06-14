# modified by Iryna Hrytsenko

import random
from functools import reduce

def decor (func):
    def inner():
        if len(filtred_list)>0:
            return func()
        else:
            return 0
    return inner


filter_p = lambda i: i % p ==0
prod = lambda a, b: a*b

@ decor
def calc():
    # if len(filtred_list)>0:
        return reduce(prod, filtred_list)
    # return 0

n = random.randint(5, 15)
print("n = ", n)
p = random.randint(1, 12)
print("p = ", p)
list_a = tuple(random.randint(-100, 100) for i in range(n))
print(list_a)

filtred_list = list(filter(filter_p, list_a))

print(f"product of els divisible by p = {calc()}")