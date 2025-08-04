lst = list()
for i in range(5) :
    a = list(map(int,input().split()))
    lst.append([i+1, sum(a)])
lst.sort(key=lambda x:x[1], reverse=True)
print(lst[0][0], lst[0][1])