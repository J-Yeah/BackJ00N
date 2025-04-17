import sys
input = sys.stdin.readline
lst = list()
n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    lst.append([a,b])
lst.sort(key = lambda x: x[1])
lst.sort(key = lambda x: x[0], reverse = True)
cnt = 0
for i in range(5, n) :
    if lst[i][0] == lst[4][0] :
        cnt += 1
    else :
        break
print(cnt)