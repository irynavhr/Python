# modified by Iryna Hrytsenko
import sys

def print_help():
    s1 = "usage1: h7t1.py "
    print(s1, sep="\n")

def deliter():
    arr = f_text.split()
    for i in arr:
        if len(i) == 1:
            arr.remove(i)
    return " ".join(arr)


known_arg = ('-h', '--help', '/?')
if len(sys.argv) == 2 and sys.argv[1] in known_arg:
    print_help()
    exit()
elif len(sys.argv) == 1:
    try:
        with open("f.txt", "r") as reader:
            f_text = reader.read()
    except:
        print("Error: file f.txt dosn`t exist")

    with open("g.txt", "w") as file:
        try:
            file.write(deliter())
        except:
            print("Error: can't find the variable f_text or it has not apropriate data type")    
        
else:
    print_help()
    exit()