import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
p.sort(reverse = True)
a = 0
for i in range(n):
    a += p[i]*(i+1)
print(a)