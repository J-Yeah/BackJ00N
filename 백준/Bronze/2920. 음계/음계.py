num_list = list(map(int, input().split()))

total = 0

for i in range(len(num_list)) :
    if num_list[i]==i+1 :
        total += 1
    elif num_list[i]==len(num_list)-i :
        total -= 1

if total > 7 :
    print("ascending")
elif total < -7 :
    print("descending")
else :
    print("mixed")
