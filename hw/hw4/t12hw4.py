import random
n = random.randint(5, 15)
print("n = ", n)
list_a = tuple(round((random.random()*20)-10, 2) for i in range(n))
print(list_a)

min_of_all = min(list_a)
abs_list = []
neg_list = []
squard_list = []
for i in range(n):
    abs_list.append(abs(list_a[i]))
    neg_list.append(list_a[i]*((-1)**(i+1)))
    squard_list.append(round(list_a[i]**2, 2))

print(f"max_of_all = {max(list_a)}")
print(f"min_of_all = {min_of_all}")
print(f"max_of_paird = {max(list_a[1::2])}")
print(f"min_of_odd = {min(list_a[::2])}")
print(f"sum_min_paird_and_max_odd = {min(list_a[1::2]) + max(list_a[::2])}")
print(f"max_of_abs = {max(abs_list)}")
print(f"max_of_neg = {max(neg_list)}")
print(f"exp = {(min_of_all**2) - min(squard_list)}")