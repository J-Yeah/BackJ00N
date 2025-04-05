import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    b1 = 35*0.3
    c1 = 25*0.3
    d1 = 40*0.3
    if b+c+d >= 55 and b >= b1 and c >= c1 and d >= d1 :
        print(a,b+c+d,"PASS")
    else :
        print(a,b+c+d,"FAIL")