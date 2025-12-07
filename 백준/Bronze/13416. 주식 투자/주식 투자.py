import sys
input = sys.stdin.readline
for _ in range(int(input())):
    total = 0
    for i in range(int(input())):
        a,b,c = map(int, input().split())
        total += max(0,a,b,c)
    print(total)