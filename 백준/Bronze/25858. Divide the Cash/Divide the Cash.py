import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = list()
for _ in range(n):
    a.append(int(input()))
for i in range(n):
    print(m*a[i]//sum(a))