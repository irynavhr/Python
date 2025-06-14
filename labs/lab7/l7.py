from functools import reduce
import sys
import winsound

def print_help():
    s1 = "usage1: demo_08_3.py args"
    s2 = "usage2: demo_08_3.py operator args"
    s3 = "usage3: demo_08_3.py key"
    s4 = "args: list of integer without separators"
    s5 = "operator: * or +"
    s6 = "key: -h or --help or /?"
    print(s1, s2, s3, s4, s5, s6, sep="\n")

def is_nuum(a):
    num = True
    for i in a:               
        if not i.isdigit():
            num = False
            break
    return num

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CRED    = '\33[31m'

known_arg = ('-h', '--help', '/?')

if len(sys.argv) == 1  :
    winsound.MessageBeep()
    print(CRED +"You didn't input arguments!"+ CEND +"\n" + CBOLD +"Please follow instructions below." + CEND)
    print_help()
    exit()

if sys.argv[1] in known_arg:
    print_help()
    exit()

if len(sys.argv) > 2 and is_nuum(sys.argv[2:]):
    if sys.argv[1]=="*":
        print(reduce(lambda x, y: int(x) * int(y), sys.argv[2:]))
        exit()
    elif sys.argv[1]=="+":
        print(sum([int(item) for item in sys.argv[2:]]))
        exit()
    
if is_nuum(sys.argv[1:]):
    print(sum([int(item) for item in sys.argv[1:]]))
    exit()

winsound.MessageBeep()
print(CRED + "Input arguments aren't correct." + CEND + "\n" + CBOLD + "Please follow instructions below." + CEND)
print_help()
# known = True
# for i in sys.argv[1:]:
#     if i not in known_arg:
#         known = False
#         break
# if not known :
#     print_help()
#     exit()