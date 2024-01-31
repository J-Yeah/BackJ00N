a = int(input())
b = int(input())
c = int(input())

num = a*b*c
num_str = str(num)

num_0 = num_1 = num_2 = num_3 = num_4 = num_5 = num_6 = num_7 = num_8 = num_9 = 0

for i in range(len(num_str)) :
    if num_str[i] == '0' :
        num_0 += 1
    elif num_str[i] == '1' :
        num_1 += 1
    elif num_str[i] == '2' :
        num_2 += 1
    elif num_str[i] == '3' :
        num_3 += 1
    elif num_str[i] == '4' :
        num_4 += 1
    elif num_str[i] == '5' :
        num_5 += 1
    elif num_str[i] == '6' :
        num_6 += 1
    elif num_str[i] == '7' :
        num_7 += 1
    elif num_str[i] == '8' :
        num_8 += 1
    elif num_str[i] == '9' :
        num_9 += 1

num_list = [num_0, num_1 , num_2 , num_3 ,num_4 ,num_5 ,num_6, num_7 ,num_8, num_9]

for i in range(len(num_list)) :
    print(num_list[i])