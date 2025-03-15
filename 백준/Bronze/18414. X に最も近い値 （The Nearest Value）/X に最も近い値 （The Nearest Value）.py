x,l,r = map(int, input().split())
a = list()
z = 100000
for i in range(l,r+1) :
    if abs(i-x) < z :
        z = abs(i-x)
        y = i
print(y)