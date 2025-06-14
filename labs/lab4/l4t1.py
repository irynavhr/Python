lst = [ [1,2,3], [4,5], [7,8,9,10] ]

# lngs = [list(reversed(i)) for i in lst]
lngs = list(range(3))
for i in range(len(lst)):
    lngs[i] = list(reversed(lst[i]))
print(f'lngs = {lngs}')