a = list(map(int, input().split()))
t = -1
for i in a :
    if i+1000 >= a[0] :
        t += 1
print(t)