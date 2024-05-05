a = input()
b = int(a)

if a.count('7') and b%7==0 :
    print("3")
elif a.count('7') and b%7!=0 :
    print("2")
elif b%7==0 :
    print("1")
else :
    print("0") 