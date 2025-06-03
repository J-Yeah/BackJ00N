import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    lst = input().strip()
    a = list(map(int, lst.split()))
    c = a.pop(0)
    b = 1
    for i in range(1,c) :
        if a[i-1]*2 > a[i] :
            b = 0
    print("Denominations:", ' '.join(map(str,a)))
    if b :
        print("Good coin denominations!")
    else :
        print("Bad coin denominations!")
    if _ != t-1 :
        print()