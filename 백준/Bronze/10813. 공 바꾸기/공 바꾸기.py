n, x = map(int, input().split())
num_list = list()

for i in range(1,n+1):
    num_list.append(i)

for i in range(1, x+1):
    a,b = map(int, input().split())
    tmp = num_list[a-1]
    num_list[a-1] = num_list[b-1]
    num_list[b-1] = tmp

for i in range(1,n+1):
    print(num_list[i-1], end=' ')