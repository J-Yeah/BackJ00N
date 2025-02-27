a,b,n = map(int, input().split())
a %= b
for _ in range(n):
    a *= 10 
    re = a//b 
    a %= b 

print(re)