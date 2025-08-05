import sys
input = sys.stdin.readline
for i in range(int(input())):
    a,b,c = map(int,input().split())
    total = 0
    for j in range(a):
        d,v = map(int, input().split())
        if d <= b*c :
            total += v
    print(f"Data Set {i+1}:")
    print(total)
    print()