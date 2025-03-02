import sys
n, w, h = map(int, sys.stdin.readline().split())
z = (w**2+h**2)**(0.5)
for i in range(n):
    a = int(sys.stdin.readline())
    if a <= z :
        print("DA")
    else :
        print("NE")