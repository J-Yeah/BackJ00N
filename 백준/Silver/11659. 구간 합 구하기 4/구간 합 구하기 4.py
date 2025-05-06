import sys
input = sys.stdin.readline
n,m = map(int, input().split())
listn = list(map(int, input().split()))
sumn = [0]
a = 0
for x in listn:
    a += x
    sumn.append(a)
for _ in range(m):
    i,j = map(int, input().split())
    print(sumn[j]-sumn[i-1])