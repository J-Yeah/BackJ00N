import sys
a = list()
for _ in range(int(sys.stdin.readline())):
    b = sys.stdin.readline().strip()
    a.append(b)
c = list(set(a))
c.sort()
c.sort(key = len)
for j in range(len(c)):
    print(c[j])