# modified by Iryna Hrytsenko

import sys

def decorr(main):
    def inner():
        if len(sys.argv) == 1:
            main()
            print("To see resolt open g.txt, please.")
        else:
            print_help()
    return inner

def print_help():
    print("Don't correct calling program!\nusage: h7ch11t3.py ")

@ decorr
def main():
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
        
main()

