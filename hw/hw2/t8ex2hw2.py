import random
n = random.randint(1, 10)
c1 = random.randint(0, 6)
c2 = random.randint(0, 6)
c3 = random.randint(0, 6)
print("n", n)
print(c1, c2, c3, "- задані користувачем залишки", sep="  ")
i = 0
dubled_odd = 0
remainder_of_division_coincided_with_num = 0
while i < n:
    i += 1
    q = random.randint(1, 100)
    print(q, end="   ")
    if q % 2 == 0 and (q//2)%2==1:
        dubled_odd += 1
    if q % 7 == c1 or q % 7 == c2 or q % 7 == c3:
        remainder_of_division_coincided_with_num += 1
print("\ndubled_odd = ", dubled_odd)
print("remainder_of_division_coincided_with_num = ", remainder_of_division_coincided_with_num)