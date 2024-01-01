num = int(input())
num_list = list()

for i in range (1, num+1):
    num_list.append(int(input()))
    num_list.sort()

for i in range(1, num+1):
    print(num_list[i-1])
