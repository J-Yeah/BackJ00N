import sys
input = sys.stdin.readline
dic = {}
n,m = map(int, input().split())
for _ in range(n):
    key, val = map(str, input().split())
    dic[key] = val

for _ in range(m):
    a = input().strip()
    print(dic[a])