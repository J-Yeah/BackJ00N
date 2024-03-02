num1, num2 = map(int, input().split())

num_list = list()
num_list2 = list()
num_list_total = list()

for i in range(num1):
    num_list.append(list(map(int, input().split())))

for i in range(num1):
    num_list2.append(list(map(int, input().split())))


for i in range(num1):
    for j in range(num2):
        num_list_total.append(num_list[i][j]+num_list2[i][j])

for i in range(num1*num2):
    print(num_list_total[i], end=' ')
    if i%num2==num2-1:
        print('')