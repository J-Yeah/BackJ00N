chess = [1,1,2,2,2,8]

che_list = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i]-che_list[i], end=' ')