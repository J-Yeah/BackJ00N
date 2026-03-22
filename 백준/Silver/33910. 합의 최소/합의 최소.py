import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

ans = 0
x = arr[n-1]

for i in range(n-1, -1, -1):
    x = min(x, arr[i])
    ans += x

print(ans)