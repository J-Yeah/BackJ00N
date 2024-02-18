import sys
num_list = list()

for i in range(5):
    a = int(sys.stdin.readline())
    if a < 40 :
        a = 40
    num_list.append(a)

print(sum(num_list)//5)