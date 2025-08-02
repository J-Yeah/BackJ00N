n, cm = map(int, input().split())
a = list(map(int, input().split()))
total = 0
for i in range(n):
    if cm >= a[i]:
        total += 1
print(total)