import math
n = int(input())
a = list(map(int, input().split()))
t, p = map(int, input().split())

shirt = 0
for i in range(len(a)):
    shirt += math.ceil(a[i]/t)

print(shirt)
print(n//p, n%p)