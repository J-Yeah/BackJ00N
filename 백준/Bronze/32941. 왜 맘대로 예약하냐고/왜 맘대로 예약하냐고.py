import sys
input = sys.stdin.readline
t,x = map(int, input().split())
n = int(input())
cnt = 0
for i in range(n):
    k = int(input())
    a = list(map(int, input().split()))
    if a.count(x) :
        cnt += 1
if cnt == n :
    print("YES")
else :
    print("NO")