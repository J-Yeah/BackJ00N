n = int(input())
a = list(map(int, input().split()))
if a[0] == 0 :
    b = [-1]
else :
    b = [1]
for i in range(1, n):
    if a[i] == 1 :
        b.append(b[-1]+1)
    elif a[i] == 0 :
        b.append(b[-1]-1)
print(sum(b))