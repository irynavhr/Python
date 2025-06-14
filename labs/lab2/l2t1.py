# 1. Розв'яжіть з глави 4 підручника [M2] завдання 1с (с. 92).
# Гриценко Ірина Валеріївна
print("Print your values for a, b, c:")
a = int(input ("\ta = "))
b = int(input ("\tb = "))
c = int(input ("\tc = "))
x = 0
if a==b or b==c or a==c :
    print("Tie")
elif a > b and a > c:
    x = a
elif b>a and b>c:
    x = b
else:
    x = c
if x != 0:
    print("The largest is:", x)