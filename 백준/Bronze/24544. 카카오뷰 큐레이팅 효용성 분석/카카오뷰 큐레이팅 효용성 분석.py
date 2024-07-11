num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total = 0

for i in range(num):
    if b[i]==0:
        total += a[i]
        
print(sum(a))
print(total)