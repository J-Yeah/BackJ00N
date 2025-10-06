n = 0
m = 0
for _ in range(10):
    o, i = map(int, input().split())
    n -= o
    n += i
    if n>m :
        m = n
print(m)