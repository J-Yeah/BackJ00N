import math
n,k = map(int, input().split())
lst = list(map(int, input().split()))
total = 0
for i in lst :
    total += math.ceil(i/2)
if total >= n :
    print("YES")
else :
    print("NO")