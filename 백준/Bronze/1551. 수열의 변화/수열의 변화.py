import sys
input = sys.stdin.readline
n,k = map(int, input().split())
a = list(map(int, input().split(',')))
x = n
for i in range(k):
    lst = list()
    for j in range(x-1):
        lst.append(a[j+1]-a[j])
    a = lst
    x -= 1
print(",".join(map(str, a)))