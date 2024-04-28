num = int(input())
for i in range(num):
    a,b,x = map(int,input().split())
    print(a*(x-1)+b)