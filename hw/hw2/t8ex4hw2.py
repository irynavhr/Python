import random
n = random.randint(1, 10)
i = 0
sum_of_divisible_by_5 = 0
sum_of_odd_and_negative = 0
sum_of_satisfing_the_condition = 0
while i < n:
    i += 1
    a = random.randint(-100, 100)
    print(a, end="   ")
    if a % 5 == 0:
        sum_of_divisible_by_5 += a
    if a % 2 == 1 and a < 0:
        sum_of_odd_and_negative += a
    if abs(a) < (i**2):
        sum_of_satisfing_the_condition += a
print("\nsum_of_divisible_by_5 = ", sum_of_divisible_by_5)
print("sum_of_odd_and_negative = ", sum_of_odd_and_negative)
print("sum_of_satisfing_the_condition = ", sum_of_satisfing_the_condition)