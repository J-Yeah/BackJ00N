import sys
input = sys.stdin.readline
max_price = 0
for i in range(int(input())):
    a,b,c = map(int, input().split())
    if a==b and a==c :
        price = 10000+a*1000
    elif a==b :
        price = 1000+a*100
    elif b==c :
        price = 1000+b*100
    elif a==c :
        price = 1000+a*100
    else :
        price = max(a,b,c)*100
    if price > max_price:
        max_price = price
print(max_price)