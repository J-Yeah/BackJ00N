import sys
num = int(sys.stdin.readline())
for i in range(num):
    s = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    opt = 0
    for j in range(n):
        q,p = map(int, sys.stdin.readline().split())
        opt += q*p
    print(s+opt)