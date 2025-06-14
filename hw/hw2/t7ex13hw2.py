import random
n = str(random.randint(1, 1000000000))
d = str(random.randint(1, 9))
print("n = ", n)
print("d = ", d)
n_memorised = n


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
x = 0
for i in n:
    if i == d:
        x += 1
if x > 0:
    print(d, " is in the number: ", n)
else:
    print(d, " is not in the number: ", n)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
my_n = n
# if n[len(n) - 1] == "0":
#     my_n = n[0:(len(n)-1):1]
rev = ""
for i in my_n:
    rev = i + rev
print("reverse order:", rev)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
first_and_last_rev = n[len(n)-1] + n[1:len(n)-1:1] +n[0]
print("first_and_last_reversed = ", first_and_last_rev)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
d_instead_of_first_and_last_didg = d + n[1:len(n)-1:1] + d
print("d_instead_of_first_and_last_didg = ", d_instead_of_first_and_last_didg)