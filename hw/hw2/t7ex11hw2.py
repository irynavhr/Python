import random
n = random.randint(1, 1000000000)
print("n = ", n)
n_memorised = n


# !!!!!!!!!!!!!!!!!!!!!!!quantity
k=1
while (n//10)!=0:
    n = n // 10
    k += 1
print("Quantity of digits of the number:",k)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Summary
n = n_memorised
sum_of_didgits = 0
while n > 0:
    sum_of_didgits += (n%10)
    n //= 10
print("Summary of digits of the number:", sum_of_didgits)


# !!!!!!!!!!!!!!!!!!!!!First didgit
n = n_memorised
while (n//10) != 0:
    n //= 10
print("First digit of the number:", n)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!exspresion
n = n_memorised
quantity_didg = k
expresion = 0
while n != 0:
    expresion += (n%10)*((-1)**(quantity_didg-1))
    n //= 10
    quantity_didg -= 1
print("Expresion with the number as variable equales:", expresion)
