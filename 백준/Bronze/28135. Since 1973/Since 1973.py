n = int(input())

cnt = 0
for i in range(n):
    cnt += 1
    if "50" in str(i) :
        cnt += 1
print(cnt)