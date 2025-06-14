# developed by Iryna Valeriivna Hrytsenko
import numpy as np
import random as rnd

n = rnd.randint(5, 10)
x_ = []
for i in range(n):
    x_.append(round(rnd.randint(100, 999), 2))
x = np.array(x_)
print(x)

max_el = int(np.max(x))
min_el = int(np.min(x))
print("max_el = ", max_el)
print("min_el = ", min_el)

print("len(x) = ", len(x))

count_min = 0
count_max = 0
for i in range(n):
    if x[i] == max_el:
        count_max+=1
    if x[i] == min_el:
        count_min+=1

if count_max == 1 and count_min == 1:
    my_min = np.where(x==min_el)[0][0]
    my_max = np.where(x==max_el)[0][0]
    x[my_min] = max_el
    x[my_max] = min_el
    print(x)
else:
    print("member of min els", count_min)
    print("member of max els", count_max)