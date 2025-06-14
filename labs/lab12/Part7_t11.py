# developed by Iryna Valeriivna Hrytsenko
import numpy as np
import random as rnd

n = rnd.randint(5, 10)
x_ = []
for i in range(n):
    x_.append(round(rnd.randint(1, 10), 2))
x = np.array(x_)
print(x)

max_el = int(np.max(x))
min_el = int(np.min(x))
print("max_el = ", max_el)
print("min_el = ", min_el)

print("len(x) = ", len(x))

# # a)
# i = 0
# l = int(len(x))
# while i < l:
#     if x[i] == max_el:
#         x = np.delete(x, i)
#         l-=1
#         continue
#     i+=1
# print("deleted max", x)

# # b)
# i = 0
# l = int(len(x))
# while i < l:
#     if x[i] == min_el:  
#         x = np.delete(x, i)
#         l-=1
#         continue
#     i+=1
# print("deleted min", x)

# # c)
# i = 0
# l = int(len(x))
# while i < l:
#     if x[i] == max_el or x[i] == min_el:
#         x = np.delete(x, i)
#         l-=1
#         continue
#     i+=1
# print("deleted max and min", x)

# # d)
# i = 0
# l = int(len(x))
# while i < l:
#     if x[i]%2 == 0:
#         x = np.delete(x, i)
#         l-=1
#         continue
#     i+=1
# print("deleted pared els", x)


# # e)
# i = 0
# l = int(len(x))
# while i < l-1:
#     if x[i+1] < x[i]:
#         x = np.delete(x, i+1)
#         l-=1
#         continue
#     i+=1
# print("unfalling", x)

# # f)
# i = 0
# l = int(len(x))
# while i < l-1:
#     if x[i+1] > x[i]:
#         x = np.delete(x, i+1)
#         l-=1
#         continue
#     i+=1
# print("ungrowing", x)

# # g)
# i = 0
# l = int(len(x))
# while i < l-1:
#     if x[i+1] <= x[i]:
#         x = np.delete(x, i+1)
#         l-=1
#         continue
#     i+=1
# print("growing", x)



# # h)
# i = 0
# l = int(len(x))
# while i < l-1:
#     if x[i+1] >= x[i]:
#         x = np.delete(x, i+1)
#         l-=1
#         continue
#     i+=1
# print("falling", x)

