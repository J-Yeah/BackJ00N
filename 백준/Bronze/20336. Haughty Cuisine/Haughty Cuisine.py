import sys
input = sys.stdin.readline
n = int(input())
b = list()
for _ in range(n):
    a = list(map(str, input().split()))
    b.append(a)
for i in range(int(b[0][0])+1):
    print(b[0][i])