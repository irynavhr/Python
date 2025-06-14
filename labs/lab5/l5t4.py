def rec_num_of_didg(num):
    if num == 0:
        return 0
    else:
        return 1 + rec_num_of_didg(num//10)
    
x = int(input("input a num, please:\t"))
print(rec_num_of_didg(x))