num, a = map(int, input().split())
num_list = list()

for i in range(1, num+1):
    num_list.append(i)

for i in range(a):
    front, ends= map(int, input().split())
    while front<ends :
        tmp = num_list[front-1]
        num_list[front-1] = num_list[ends-1]
        num_list[ends-1] = tmp
        front += 1
        ends -= 1

for i in range(1, num+1):
    print(num_list[i-1], end=' ')