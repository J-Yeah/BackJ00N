import sys
input = sys.stdin.readline
n,m = map(int, input().split())
lis = set()
for i in range(n):
    lis.add(input().strip())
see = set()
for j in range(m):
    see.add(input().strip())
a = list(see & lis)
a.sort()
print(len(a))
for x in range(len(a)):
    print(a[x])