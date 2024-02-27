import sys

x,y = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for i in range (5):
    print(a[i]-x*y, end=' ')