import random
n = random.randint(3, 5)
my_nums = [round(random.random()*100, 3) for i in range(n)]
n = random.randint(3, 5)
k = random.randint(2, 5)
my_lists = [[round(random.random()*100, 3) for i in range(k)] for e in range(n)]
my_data = my_lists + my_nums
random.shuffle(my_data)
print(f"\nmy_data:\n{my_data}")
del my_lists, my_nums
def sum_count(*args):
    s = 0
    for i in args:
        if type(i) == list:
            for j in i:
                s += j
        else:
            s += i
    return s
print(f"\nsum is: {sum_count(*my_data)}\n")