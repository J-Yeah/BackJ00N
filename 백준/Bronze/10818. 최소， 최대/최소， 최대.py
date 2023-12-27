N = int(input())
num_list=list(map(int, input().split()))

Min = num_list[0]
Max = num_list[0]

for i in range(1,N):
    if (Min > num_list[i]) :
        Min = num_list[i]
    else :
        pass

for i in range(1,N):
    if (Max < num_list[i]) :
        Max = num_list[i]
    else :
        pass

print(Min, Max)
