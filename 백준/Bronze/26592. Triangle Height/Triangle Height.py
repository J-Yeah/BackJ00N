import sys
for _ in range(int(sys.stdin.readline())):
    a,b = map(float, sys.stdin.readline().split())
    h = (a*2)/b
    print(f"The height of the triangle is {h:.2f} units")