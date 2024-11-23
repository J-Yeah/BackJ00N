import sys
for i in range(int(sys.stdin.readline())):
    a = list(sys.stdin.readline().strip())
    if len(a)==1 :
        print(*a)
    else :
        for j in range(len(a)-1, 0, -1):
            if int(a[j]) >= 5 :
                a[j-1] = str(int(a[j-1])+1)
                a[j] = '0'
            else :
                a[j] = '0'
        print(*a, sep='')