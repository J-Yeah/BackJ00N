a = 0
b = list()
for i in range(7):
    n = int(input())
    if n %2 == 1 :
        a += n
        b.append(n)
if a == 0 :
    print(-1)
else :
    print(a)
    b.sort()
    print(b[0])