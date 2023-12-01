a,b=input().split()
a=int(a)
b=int(b)

c =int(input())

d=b+c
while d>59 :
    if d>59 :
        if a==23:
            a=0
            d-=60
        else:
            a+=1
            d-=60

print(a,d)
