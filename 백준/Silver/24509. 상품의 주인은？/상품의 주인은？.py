import sys
input = sys.stdin.readline
n = int(input())
x = list()
for _ in range(n):
    a = list(map(int, input().split()))
    x.append(a)
for i in range(1,5):
    x.sort(key=lambda x: x[0])
    x.sort(key=lambda x: x[i], reverse = True)
    print(x[0][0], end=' ')
    x.pop(0)