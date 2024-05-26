print("Gnomes:")
num = int(input())
for i in range(num) :
    lst = list(map(int, input().split()))
    result = True
    if (lst[2] - lst[1] >= 0 and lst[1] - lst[0] >= 0) or (lst[2] - lst[1] < 0 and lst[1] - lst[0] < 0) :
        print("Ordered")
    else :
        print("Unordered")