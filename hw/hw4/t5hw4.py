import random
n = random.randint(5, 15)
print("n = ", n)

list_a = tuple(random.randint(-100, 100) for i in range(n))
print(list_a)

quantity = 0
sum_of_els = 0

for i in list_a:
    if i % 5 == 0 and i % 7 != 0:
        quantity +=1
        sum_of_els += i
print(f"quantity = {quantity}")
print(f"sum of elements = {sum_of_els}")