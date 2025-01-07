import sys
for i in range(int(sys.stdin.readline())):
    a = list()
    b = list()
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for j in range(1, n+1):
    	b.append(j)
    a.append(b)
    if n == 1 :
        print(1)
    else :
        for x in range(1,k+1):
            c = [1]
            for y in range(1, n):
                d = a[x-1][y]+c[y-1]
                c.append(d)
            a.append(c)
        print(a[k][n-1])