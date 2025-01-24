import sys
lst = list()
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip()
    b = a[0:3]
    if b == "pus" :
        c, d = a.split()
        lst.append(d)
    elif b == "pop" :
        try :
            print(lst.pop())
        except :
            print(-1)
    elif b == "siz" :
        print(len(lst))
    elif b == "emp" :
        if len(lst) :
            print(0)
        else :
            print(1)
    elif b == "top" :
        if len(lst) :
            print(lst[-1])
        else :
            print(-1)