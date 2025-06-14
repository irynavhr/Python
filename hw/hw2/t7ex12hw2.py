import random
n = random.randint(1, 1000000000)
m = random.randint(1, 18)
print("n = ", n)
print("m = ", m)
n_memorised = n


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!сума останніх m цифр
k = 0
sum_of_last = 0
while k < m:
    sum_of_last += n%10
    n //= 10
    k += 1
print("sum_of_last = ", sum_of_last)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!сума перших m цифр
n = n_memorised
q = 1
while (n//10)!=0:
    n = n // 10
    q += 1

changeable_didgit_Q = q
n = n_memorised
counter = 0
limit = min(m, q)
sum_of_first = 0
while counter < limit:
    sum_of_first += n//(10**(changeable_didgit_Q - 1))
    n %= (10**(changeable_didgit_Q - 1))
    changeable_didgit_Q -= 1
    counter += 1
print("sum_of_first = ", sum_of_first)