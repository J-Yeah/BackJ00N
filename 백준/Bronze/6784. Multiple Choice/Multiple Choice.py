import sys
input = sys.stdin.readline

n = int(input())
lst = [input().strip() for _ in range(n)]
ans = 0
for i in range(n) :
    if lst[i] == input().strip() :
        ans += 1
print(ans)