import random
n = random.randint(1, 1000000000)
d = random.randint(0, 9)
# k = random.randint(0, 9)                    # (14.b)    unlock to delete two didgits from the number.
# p = random.randint(0, 9)                    # (14.c)    unlock this block to delete two didgits from the number  AND  put q-didgits instead of p-didgits.
# q = random.randint(0, 9)                    # (14.c)    unlock this block to delete two didgits from the number  AND  put q-didgits instead of p-didgits.
print("n = ", n)
print("d = ", d)
# print("k = ", k)                            # (14.b)    unlock to delete two didgits from the number.
# print("p = ", p)                            # (14.c)    unlock this block to delete two didgits from the number  AND  put q-didgits instead of p-didgits.
# print("q = ", q)                            # (14.c)    unlock this block to delete two didgits from the number  AND  put q-didgits instead of p-didgits.


# calculating quantity_of_didg:
quantity_of_didg = 0
num = n
while num!=0:
    quantity_of_didg += 1
    num //= 10
# print("quantity_of_didg", quantity_of_didg)


# making n without d-didgits:
i = 0
while i < quantity_of_didg:
    didg = (n % (10**(i+1))) // (10**(i))
    if didg == d:
        n = (n//(10**(i+1)))*(10**(i)) + n % (10**(i))
        quantity_of_didg -= 1
        continue
    i += 1
print("n without d-didg = ", n)


# making n without d-didgits and k-didgits:            # (14.b)    unlock this block to delete two didgits from the number.
# i = 0
# while i < quantity_of_didg:
#     didg = (n % (10**(i+1))) // (10**(i))
#     if didg == k:
#         n = (n//(10**(i+1)))*(10**(i)) + n % (10**(i))
#         quantity_of_didg -= 1
#         continue
#     i += 1
# print("n without d-didg and k-didg = ", n)


# making n with q-didgits instead of p-didgits:            # (14.c)    unlock this block to delete two didgits from the number  AND  put q-didgits instead of p-didgits.
# i = 0
# while i < quantity_of_didg:
#     didg = (n % (10**(i+1))) // (10**(i))
#     if didg == p:
#         n = ((n//(10**(i+1)))*10 + q)*(10**(i)) + n % (10**(i))
#     i += 1
# print("n without d-didg and k-didg = ", n)