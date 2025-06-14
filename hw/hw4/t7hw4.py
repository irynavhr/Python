import random
n = random.randint(5, 15)
print("n = ", n)
list_a = tuple(round((random.random()*20)-10, 2) for i in range(n))
print(list_a)

sum = 0
for i in list_a:
    if i > 0:
        sum += i
print(f"duobled sum = {sum*2}")