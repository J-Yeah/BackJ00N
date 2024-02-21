import sys

N = int(sys.stdin.readline())
an = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
am = list(map(int, sys.stdin.readline().split()))

for i in range(len(am)) :
    if am[i] in an :
        print(1)
    else :
        print(0)