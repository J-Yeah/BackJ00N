t = int(input())
a = list(map(int, input().split()))
for _ in range(5-t):
    a.append(0)
total = 0
if a[0] > a[2] :
    total += (a[0]-a[2])*508
else : 
    total += (a[2]-a[0])*108
if a[1] > a[3] :
    total += (a[1]-a[3])*212
else :
    total += (a[3]-a[1])*305
total += a[4]*707
print(total*4763)