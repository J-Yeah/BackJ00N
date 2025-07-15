n,k = map(int, input().split())
x = list()
for i in range(1,n+1):
    if n%i == 0 :
        x.append(i)
try :
    print(x[k-1])
except :
    print(0)