import random
n = random.randint(1, 10)
i = 0
num_odd = 0
is_divisible_by_3_and_not_5 = 0
is_squared = 0
is_odd_and_have_paired_order = 0
while i < n:
    i += 1
    a = random.randint(1, 100)
    print(a, end="   ")
    if a % 2 == 1:
        num_odd += 1
    if a % 3 == 0 and a % 5 != 0:
        is_divisible_by_3_and_not_5 += 1
    if a == (int(a**0.5))**2:
        is_squared += 1 
    
    if i % 2 == 0 and a % 2 == 1:
        is_odd_and_have_paired_order += 1
print("\nnum_odd = ", num_odd)
print("is_divisible_by_3_and_not_5 = ", is_divisible_by_3_and_not_5)
print("is_squared = ", is_squared)
print("is_odd_and_have_paired_order = ", is_odd_and_have_paired_order)

num_that_satisfies_the_condition = 0
a1 = random.randint(1, 100)
a2 = random.randint(1, 100)
a3 = random.randint(1, 100)
print(a1, a2, a3, sep="   ", end="   ")
k = 0
while k < (n-2):
    k += 1
    if a2 < (a1 +a3)/2:
        num_that_satisfies_the_condition += 1
    a1 = a2 
    a2 = a3
    a3 = random.randint(1, 100)
    print(a3, end="   ")
print("num_that_satisfies_the_condition = ", num_that_satisfies_the_condition)