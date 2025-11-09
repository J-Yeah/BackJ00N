import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

res = 0
for i in range(1, len(x) + 1):
    for j in range(i, i + 1):
        lemon = x[i - 1]
        tmp = lemon - (n + 1 - i)
        res = max(res, tmp)
print(res)