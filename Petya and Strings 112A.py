# Petya and Strings 112A

string1=str(input())
string2=str(input())
x = string1.lower()
y = string2.lower()
if x==y:
    print("0")
elif x>y:
    print("1")
else:
    print("-1")