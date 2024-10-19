n, k, p = map(int, input().split())
bread = list(map(int, input().split()))

total= 0
for i in range(n):
    if sum(bread[i*k:i*k+k])>=p :
        total += 1

print(total)