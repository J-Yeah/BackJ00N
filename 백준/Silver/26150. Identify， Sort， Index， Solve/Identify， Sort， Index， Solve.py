import sys
n = int(sys.stdin.readline())
a = list()
z = ""
for _ in range(n):
    y = sys.stdin.readline().split()
    a.append(y)
a.sort(key = lambda x : int(x[1]))
for j in range(n):
    d = int(a[j][2])
    z += a[j][0][d-1]
z = z.upper()
print(z)