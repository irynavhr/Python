# modified by Iryna Hrytsenko

import random
from functools import reduce

n = random.randint(5, 15)
print("n = ", n)
list_a = tuple(round((random.random()*20)-10, 2) for i in range(n))
print(list_a)

pos_list = list(filter(lambda x: x>=0, list_a))
neg_list = list(filter(lambda x: x<0, list_a))
print(pos_list)
print(neg_list)
sum_of_pos = reduce(lambda a, b:a+b, pos_list)

print(pos_list)

print(f"sum of pos = {(sum_of_pos)}")
print(f"quantity of neg = {len(neg_list)}")