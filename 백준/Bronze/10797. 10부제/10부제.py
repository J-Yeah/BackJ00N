num = int(input())
a = list(map(int, input().split()))
total = 0
for i in range (5):
    if num==a[i]%10:
        total += 1
print(total)