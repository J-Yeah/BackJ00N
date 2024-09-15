n = int(input())
bread = 1001
for i in range(n):
    a,b = map(int,input().split())
    if a<b :
        if bread > b :
            bread = b

if bread > 1000 :
    print(-1)
else :
    print(bread)