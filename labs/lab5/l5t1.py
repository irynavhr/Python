x = int(input("input a num, please:\t"))
def len_num(num):
    k = 0
    t = num
    while t>0:
        t //= 10
        k += 1
    return k

def is_num_palindrom (num):
    kilk = len_num(num)
    print(kilk)
    arr_of_didg = []
    for i in range(kilk):
        arr_of_didg.append(num%10)
        num //= 10
    print(arr_of_didg)
    arr = arr_of_didg[:]
    arr_of_didg.reverse()
    print(arr_of_didg)
    print("tuples:")
    print(tuple(arr_of_didg))
    print(tuple(arr))
    # return True if tuple(arr_of_didg) == tuple(arr) else False     tuples are not needed
    return True if arr_of_didg == arr else False
print(is_num_palindrom(x))