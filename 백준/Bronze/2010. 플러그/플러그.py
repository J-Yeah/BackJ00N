import sys
input = sys.stdin.readline
n = int(input())
total = 0
for _ in range(n):
    a = int(input())
    total += a
print(total - n + 1)