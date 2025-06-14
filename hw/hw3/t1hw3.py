import random
n = random.randint(10, 20)
i = 0
list1 = []
while i < n:
    i += 1
    list1.append(random.randint(1, 100))
print(list1, len(list1))

num_odd = 0
is_divisible_by_3_and_not_5 = 0
is_squared = 0
num_that_satisfies_the_condition = 0
is_odd_and_have_paired_order = 0 

for i in list1:
    if i % 2 == 1:
        num_odd += 1
    if i % 3 == 0 and i % 5 != 0:
        is_divisible_by_3_and_not_5 += 1
    if i == (int(i**0.5))**2:
        is_squared += 1 
   
for i in range(n-2):
    if list1[i+1] < (list1[i] + list1[i+2])/2:
        num_that_satisfies_the_condition += 1

for i in range(n):
    if i % 2 == 1 and list1[i] % 2 == 1:
     is_odd_and_have_paired_order += 1

print("\nnum_odd = ", num_odd)
print("is_divisible_by_3_and_not_5 = ", is_divisible_by_3_and_not_5)
print("is_squared = ", is_squared)
print("num_that_satisfies_the_condition = ", num_that_satisfies_the_condition)
print("is_odd_and_have_paired_order = ", is_odd_and_have_paired_order)


