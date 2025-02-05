import sys
for _ in range(int(sys.stdin.readline())):
    a = list(map(int, sys.stdin.readline().split()))
    print(sum(a))