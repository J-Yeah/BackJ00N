import sys
for _ in range(int(sys.stdin.readline())):
    c, p = map(int, sys.stdin.readline().split())
    print(c,p)
    print(p+((c-1)*(p-2)))