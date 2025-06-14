# developed by Iryna Valeriivna Hrytsenko
import numpy as np
import random as rnd

n = rnd.randint(10, 20)
b_ = []
for i in range(n):
    b_.append(round(rnd.random()*10, 2))
print("b_", b_)


b = np.array(b_)
print(b)
sum = 0
for i in range(n):
    sum += b[i]
print(sum)
# print(b)

a_ = []
for i in b:
    a_.append(round((sum-i)/(n-1), 2))
a = np.array(a_)
print("a_", a_)
a = np.append(a, [111])
print(a)