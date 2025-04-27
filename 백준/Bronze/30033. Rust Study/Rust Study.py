n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
for i in range(n):
    if a[i] <= b[i] :
        s += 1
print(s)