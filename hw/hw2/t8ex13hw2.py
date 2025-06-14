import random
n = random.randint(1, 10)
i = 0
neg = 0
pos = 0
end_0_to_4 = 0
end_5_to_9 = 0
while i < n:
    i += 1
    a = random.randint(-100, 100)
    print(a, end="   ")
    if a % 10 >= 0 and a % 10 < 5:
        end_0_to_4 += 1
    else:
        end_5_to_9 += 1
    if a < 0:
        neg += 1
    elif a > 0:
        pos += 1
    
print("\nQuantity of negetive is more than positive one: ", neg > pos)
print("Quantity of nums ending on 0, 1, 2, 3, 4 is more than others: ", end_0_to_4 > end_5_to_9)