A, B, N = map(int, input().split())
a = 10000
for i in range(N):
    cost, num = map(int, input().split())
    lst = list(map(int, input().split()))
    try:
        lst.index(B, lst.index(A))
        if a > cost :
            a = cost
    except :
        pass
    
if a < 1001:
    print(a)
else:
    print(-1)