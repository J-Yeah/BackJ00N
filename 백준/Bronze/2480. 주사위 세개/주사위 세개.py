a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)

if a==b and b==c :
    print(10000+a*1000)
elif a==b or b==c :
    print(1000+b*100)
elif a==c :
    print(1000+a*100)
else :
    if a>=b and a>=c :
        print(a*100)
    elif b>=a and b>=c :
        print(b*100)
    else :
        print(c*100)
