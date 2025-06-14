import random
n = random.randint(5, 10)
my_nums = [round(random.random()*100, 3) for i in range(n)]
print(my_nums)
def sum_count(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_count(*my_nums))