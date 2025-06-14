def sum_count(*args):
    s = 0
    for i in args:
        s += i
    return s
import random
# генерація масиву
n = random.randint(10, 20)
current_list = [i for i in range(1, n)]                         # variant 1
# current_list = [random.randint(1, 20) for i in range(1, n)]       # variant 2
current_list.sort(reverse=True)
print(current_list)
# оголошення деяких змінних
lim = sum_count(*tuple(current_list))/2
print(f"Полловина суми поточного списку = {lim}")
a = []
i=0
k = n-1
# цикл який виконує всю роботу
while i<k:
    if sum_count(*a) + current_list[i] <= lim:
        a.append(current_list[i])
        current_list.remove(current_list[i])
        k -= 1
    else:
        i +=1
b = current_list[:]
print(a, "\t", sum_count(*a))
print(b, "\t", sum_count(*b))