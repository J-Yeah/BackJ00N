import sys
input = sys.stdin.readline
n = int(input())
x,s = map(int, input().split())
for i in range(n):
    c,p = map(int, input().split())
    if c <= x and p > s :
        print("YES")
        exit()
print("NO")