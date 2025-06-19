import sys
input = sys.stdin.readline
n,m = map(int, input().split())
cnt = 0
for _ in range(n):
    a = input().strip()
    if a.count('O')>a.count('X'):
        cnt += 1
print(cnt)