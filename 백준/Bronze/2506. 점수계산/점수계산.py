n = int(input())
lst = list(map(int, input().split()))
total = 0
cnt = 1
for i in lst :
    if i == 1 :
        total += cnt
        cnt += 1
    else :
        cnt = 1
print(total)