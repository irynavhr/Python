import random 
from time import time 
t0 = time()

# утворюємо список цифр:
mySet = list(range(1,10))
# print(f"my mySet is: {mySet}")

# утворюємо список майбутніх чисел:
list_of_nums = []

# безпосереднє утворення та додавання числа до списку:
for e in range(10):
    # перемішуємо цифри в списку:
    random.shuffle(mySet)
    # print(f"my mySet is: {mySet}")

    # вирізаємо 5 елементів:
    prep_didg_list = mySet[:5]
    # print(f"my prep_list is: {prep_list}")

    # перетворюємо список на дробове число:
    num = 0
    for i in prep_didg_list:
        # num = num*10 + i
        num *= 10
        num += i
    num /= 100000

    # додаємо число в список
    list_of_nums.append(num) 



# відлік часу завершено
t = time() - t0
print(f"\ntime is: {t}")
# вивід списку
print(f"\nmy list_of_nums is: {list_of_nums}") 







