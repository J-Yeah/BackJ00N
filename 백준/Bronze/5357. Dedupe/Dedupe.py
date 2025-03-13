import sys
n = int(sys.stdin.readline())
for i in range(n):
    a = sys.stdin.readline().strip()
    s = ''
    for j in range(len(a)-1):
        if a[j] != a[j+1]:
            s += a[j]
    if len(a) > 0:
        s += a[-1]
    print(s)