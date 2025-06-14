import random
x = round(random.random()*10, 2)
y = round(random.random()*10, 2)
z = round(random.random()*10, 2)

print("\nTask3")
print("x = ", x, "\ty = ", y, "\tz = ", z)
m = round(max((x+y+z), (x*y*z)), 2)
n = round(min((x+y+(z/2)), (x*y*z)), 2)
print("a) ",m,"\nб) ", n)

print("\nTask4")
print("a = ", x, "\tb = ", y, "\tc = ", z)
if x < y and y < z:
    print(True)
else: 
    print(False)

print("\nTask6")
print("a = ", x, "\tb = ", y, "\tc = ", z)
print("This numbers are beetwen 1 and 3:")
i = 0
if x > 1 and x < 3:
    print("\ta = ", x)
    i += 1 
if y > 1 and y < 3:
    print("\tb = ", y)
    i += 1 
if z > 1 and z < 3:
    print("\tc = ", z)
    i += 1 
if i==0:
    print("\tNone")
