import sys
lst = [25,10,5,1]
for _ in range(int(input())):
    a = list()
    n = int(input())
    for i in lst :
        b = n//i
        a.append(b)
        n = n - (b*i)
    print(a[0], a[1], a[2], a[3])