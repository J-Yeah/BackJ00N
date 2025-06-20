import sys
input = sys.stdin.readline
n = int(input())
a = int(input())
for i in range(n-1):
    a += int(input())
print(a)