import sys
for _ in range(int(sys.stdin.readline())):
    a,b,c = map(int, sys.stdin.readline().split())
    if c-b <= 0 :
        print(0)
    else :
        if a == 1 :
            print(c-b)
        elif a == 2 :
            print((c-b)*3)
        elif a == 3 :
            print((c-b)*5)