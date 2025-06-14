x = int(input("input a num, please:\t"))
def len_num(num):
    k = 0
    t = num
    while t:
        t //= 10
        k += 1
    return k
print(len_num(x))