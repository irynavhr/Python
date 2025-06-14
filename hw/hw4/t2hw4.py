import random
n = random.randint(5, 15)
list_q = tuple(random.randint(1, 50) for i in range(n))
print(list_q)

c1 = random.randint(0, 6)
c2 = random.randint(0, 6)
c3 = random.randint(0, 6)
print("n = ", n)
print(c1, c2, c3, "- задані користувачем залишки", sep="  ")

dubled_odd = 0
remainder_of_division_coincided_with_num = 0
for i in list_q:
    if i % 2 == 0 and (i//2)%2==1:
        dubled_odd += 1
    if i % 7 == c1 or i % 7 == c2 or i % 7 == c3:
        remainder_of_division_coincided_with_num += 1


print("dubled_odd = ", dubled_odd)
print("remainder_of_division_coincided_with_num = ", remainder_of_division_coincided_with_num)