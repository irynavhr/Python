def opp(a):
    na =""
    for i in a:
        na += str(9-int(i))
    return na

def find_amount(sym, curstr):
    counter = 0
    for i in curstr:
        if i == sym:
            counter +=1
    return counter

def rev(x):
    return x[::-1]

def deliter(x, *args):
    for i in args:
        x = x.replace(i, "")
    return x


print("\n#1", "-"*20)
string1 = "543678219"
print(f"start-string: {string1}\nformated string: {opp(string1)}")

print("\n#2", "-"*20)
string2 = "kajsdnvi!!!_uaup;ajk&hv!!n;osyfj80?9jlwk3l1kjh!f4cbk_!!!!"
cur_sym = "!"
print(f"{string2}\nSymbol '{cur_sym}' is used {find_amount(cur_sym, string2)} times")

print("\n#3", "-"*20)
string3 = "kajsdnvi!!!_uaup;ajk&hv!!n;osyfj80?9jlwk3l1kjh!f4cbk_!!!!"
cur_sym = "!"
k = find_amount(cur_sym, string3)
print(f"{string3}\nSymbol '{cur_sym}' is used {k} times")
print(str(k) + string3)

print("\n#4", "-"*20)
string4 = "Hello 123456789"
print(f"start-string4: {string4}\nreversed string4: {rev(string4)}")

print("\n#5", "-"*20)
string5 = "jjjjj5432vmlkjkj6654hhhh321cggsikj39y^*@b2j3nlkn$#*4090&0(^$##&^)"
els_need_del = ("j", "*", "4", "k")
print(string5)
print(els_need_del)
print(deliter(string5, *els_need_del))