import random
myList = []
i=0
while i < 100:
    myList.append(random.randint(20,40))
    i += 1
print(f"\ninitial list = \n{myList}")
value_zero = myList[0]

# # 1)
# while value_zero in myList:
#     del myList[myList.index(value_zero)]
# print(f"\n1)  list without {value_zero}-values = \n{myList}")

# 2)
# while value_zero in myList:
myList.remove(value_zero)
print(f"\n2)  list without {value_zero}-values = \n{myList}")