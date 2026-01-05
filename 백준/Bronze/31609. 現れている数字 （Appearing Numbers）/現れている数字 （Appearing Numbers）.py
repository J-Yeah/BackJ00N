n = int(input())
lst = list(map(int,input().split()))
result = sorted(set(lst))
for i in result :
    print(int(i))