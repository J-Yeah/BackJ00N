a,b = map(int, input().split())
prize = int(input())

if (a+b)>=prize*2 :
    print((a+b)-prize*2)
else :
    print(a+b)