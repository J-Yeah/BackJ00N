import sys
t = int(sys.stdin.readline())
for i in range(t):
    n,k = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))
    total = 0
    for j in range(n):
        total += s[j]//k
    print(total)