n, x = map(int, input().split())
num_list = list()

for i in range(1,n+1):
    num_list.append(0)

for i in range (1,x+1):
    a,b,c = map(int, input().split())
    for j in range (a, b+1):
        num_list[j-1] = c

for i in range(1, n+1):
    print(num_list[i-1], end=' ')