num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
anum = 0
bnum = 0

for i in range(num) :
    for j in range(num) :
        if a[j]<b[i] :
            anum += 1
        elif a[j]>b[i] :
            bnum += 1

if anum > bnum :
    print("second")
elif bnum > anum :
    print("first")
else :
    print("tie")