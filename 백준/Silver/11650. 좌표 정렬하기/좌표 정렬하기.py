import sys
n = int(sys.stdin.readline())
a = list()
for i in range(n):
    b = list(map(int,sys.stdin.readline().split()))
    a.append(b)
a.sort()
for j in range(n):
    print(a[j][0], a[j][1])