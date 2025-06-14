from time import time 
list = list(range(1000))
num1 = 0
num2 = 0

t0_1 = time()
for i in list:
    num1 = num1*10 + i
t1 = time() - t0_1
print(f"\ntime is: {t1}")

t0_2 = time()
for i in list:
    num2 *= 10
    num2 += i
t2 = time() - t0_2
print(f"\ntime is: {t2}")