def leapyear():
    t_leapyear = list()
    for i in range(int(x), int(y)+1):
        if i%4==0 and i%100!=0:
            t_leapyear.append(i)
    print(tuple(t_leapyear)) 

x = input("Input a start year")
y = input("Input a end year")
leapyear()