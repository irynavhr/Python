import random
n = random.randint(5, 15)
print("n = ", n)
list_a = tuple(round((random.random()*20)-10, 2) for i in range(n))
print(list_a)

sum_of_pos= 0
quant_of_neg = 0
for i in list_a:
    if i < 0:
        quant_of_neg += 1
    else:
        sum_of_pos += i
print(f"sum of pos = {sum_of_pos}")
print(f"quantity of neg = {quant_of_neg}")