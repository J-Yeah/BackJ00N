a, b = map(int, input().split())

c = a - a*b*0.01

if c >= 100 :
    print(0)
else :
    print(1)