a,n = map(int, input().split())
for _ in range(n):
    if a%2 == 0 :
        a = (a//2) ^ 6
    else :
        a = (2*a) ^ 6
print(a)