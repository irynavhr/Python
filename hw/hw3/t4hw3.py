import random
n = random.randint(5, 15)
i = 0
list_a = []
while i < n:
    i += 1
    list_a.append(random.randint(-100, 100))
print(list_a)
print("n = ", n)

sum_of_divisible_by_5 = 0
sum_of_odd_and_negative = 0
sum_of_satisfing_the_condition = 0

for i in range(n):

    if list_a[i] % 5 == 0:
        sum_of_divisible_by_5 += list_a[i]
    if list_a[i] % 2 == 1 and list_a[i] < 0:
        sum_of_odd_and_negative += list_a[i]
    if abs(list_a[i]) < (i**2):
        sum_of_satisfing_the_condition += list_a[i]

print("\nsum_of_divisible_by_5 = ", sum_of_divisible_by_5)
print("sum_of_odd_and_negative = ", sum_of_odd_and_negative)
print("sum_of_satisfing_the_condition = ", sum_of_satisfing_the_condition)