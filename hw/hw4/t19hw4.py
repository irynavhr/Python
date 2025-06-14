import random
n = random.randint(1, 7)
print("n = ", n)
list_a = tuple(round((random.random()*20)-10, 2) for i in range(n))
print(f"list_a = {list_a}")

sorted_list = list(list_a[:])
sorted_list.sort(reverse = True)
print(f"sorted_list = {sorted_list}")
print(f"list_a = sorted_list: {list_a == sorted_list}")