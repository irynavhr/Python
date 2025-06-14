# modified by Iryna Hrytsenko
import sys

def print_help():
    s1 = "usage1: h7t1.py "
    print(s1, sep="\n")


known_arg = ('-h', '--help', '/?')
if len(sys.argv) == 2 and sys.argv[1] in known_arg:
    print_help()
    exit()

elif len(sys.argv) == 1:
    try:
        with open("f.txt", "r") as reader:
            my_text = reader.read()
    except:
        print("Error: file f.txt dosn`t exist")
    
    try:
        with open("g.txt", "w") as file:
            file.write("".join(reversed(my_text)))
    except:
        print("Error: can't find the variable my_text or it has not apropriate data type")
        
else:
    print_help()
    exit()