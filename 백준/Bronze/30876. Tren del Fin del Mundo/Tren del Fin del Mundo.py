import sys
input = sys.stdin.readline
minx = 0
miny = 1001
for _ in range(int(input())):
    x,y = map(int, input().split())
    if y < miny :
        minx = x
        miny = y
print(minx,miny)