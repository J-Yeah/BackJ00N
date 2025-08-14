a,b,c = map(int, input().split())
a = a**2
b = b**2
c = c**2
if a+b==c or b+c==a or a+c==b :
    print(1)
elif a==b and a==c :
    print(2)
else :
    print(0)