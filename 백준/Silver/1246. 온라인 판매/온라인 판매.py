import sys
n,m = map(int, sys.stdin.readline().split())
a = list()
for _ in range(m):
    x = int(sys.stdin.readline())
    a.append(x)
a.sort(reverse=True)
y = 0
z = 0
for i in range(m):
    if i >= n :
        b = a[i]*n
    else :
        b = a[i]*(i+1)
    if b >= z :
        z = b
        y = a[i]
print(y,z)