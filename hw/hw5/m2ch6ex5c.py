import math
def prime(x):
    for i in range(2,round(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

print(prime(13))
print(prime(997))
print(prime(100))