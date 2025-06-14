import random
n = random.randint(5, 15)
print("n = ", n)
a = round(random.random()*(-10), 2)
b = round(random.random()*10, 2)
print(f"Заданий проміжок [{a}, {b}]")

list_a = tuple(round((random.random()*20)-10, 2) for i in range(n))
print(list_a)

quant_of_neg = 0
quant_of_belonging_to_interval = 0
for i in list_a:
    if i < 0:quant_of_neg += 1
    if i >= a and i <= b: quant_of_belonging_to_interval += 1
print(f"quantity of neg = {quant_of_neg}")
print(f"quantity of els that are in [{a}, {b}] = {quant_of_belonging_to_interval}")