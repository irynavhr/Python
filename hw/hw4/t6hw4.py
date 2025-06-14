import random
n = random.randint(5, 15)
print("n = ", n)

p = random.randint(1, 12)
print("p = ", p)

list_a = tuple(random.randint(-100, 100) for i in range(n))
print(list_a)

product_of_els_divisible_by_p = 1
for i in list_a:
    if i % p ==0:
        product_of_els_divisible_by_p *= i
print(f"product of els divisible by p = {product_of_els_divisible_by_p}")