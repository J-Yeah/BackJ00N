import sys
n = int(sys.stdin.readline())
for i in range(n):
    a1, p1 = map(int, sys.stdin.readline().split())
    r1, p2 = map(int, sys.stdin.readline().split())
    a2 = r1**2*(3.14)
    if a1/p1 > a2/p2 :
        print("Slice of pizza")
    else :
        print("Whole pizza")