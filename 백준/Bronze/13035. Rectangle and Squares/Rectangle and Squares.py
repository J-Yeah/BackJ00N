import sys
num = int(sys.stdin.readline())
for i in range(num) :
    a, b, c = map(int, sys.stdin.readline().split())
    s = round(a*b/c**2)
    if s < 1 :
        s = 1
    print((c**2)*s)