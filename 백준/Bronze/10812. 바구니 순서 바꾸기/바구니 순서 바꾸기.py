import sys

n, m = map(int, sys.stdin.readline().split())
lst = [x + 1 for x in range(n)]

for _ in range (m) :
    i, j, k = map(int, sys.stdin.readline().split())
    for y in range(k-i):
        tmp = lst.pop(i-1)
        lst.insert(j-1, tmp)
for z in range(len(lst)):
    print(lst[z], end=' ')