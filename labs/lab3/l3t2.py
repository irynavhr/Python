amount_iterations = 10
aList = list(range(amount_iterations))
print(f"aList = {aList}")

# 1 спосіб
bList = aList[::-1]
print(f"bList = {bList}")

# 2 спосіб
cList = []
i = amount_iterations
while i > 0:
    cList.append(aList[i-1])
    i -= 1
print(f"cList = {cList}")

# 3 спосіб
dList = []
k = 0
while k < amount_iterations:
    dList.append(aList.pop())
    k += 1
print(f"dList = {dList}")