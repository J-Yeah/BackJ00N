import sys
input = sys.stdin.readline
m = 0
for _ in range(int(input())):
    h,w = map(int, input().split())
    m = max(m, h*w)
print(m)