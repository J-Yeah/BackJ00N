import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c = map(str, input().split())
    print(a[:int(b)]+a[int(c):])