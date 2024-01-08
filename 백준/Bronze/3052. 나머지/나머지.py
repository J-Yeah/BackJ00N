num = int(input())
num_list = list()
num_list.append(num%42)

for i in range(1, 10):
    num = int(input())
    if (num_list.count(num%42)) == 0 :
        num_list.append(num%42)

print(len(num_list))