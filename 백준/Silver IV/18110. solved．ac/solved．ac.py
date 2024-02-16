import sys
num = int(sys.stdin.readline())

def round(n):
    if n-int(n) >= 0.5 :
        return int(n)+1
    else :
        return int(n)

if num == 0 :
    print(0)

else :
    s = round(num*0.15)

    num_list = list()
    for i in range(num) :
        a = int(sys.stdin.readline())
        num_list.append(a)

    num_list.sort()
    num_list = num_list[s:num-s]

    print(round(sum(num_list)/len(num_list)))