import sys
for i in range(int(sys.stdin.readline().strip())):
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.pop(0)
    b.pop(0)
    if a.count(4) > b.count(4):
        print("A")
    elif a.count(4) < b.count(4):
        print("B")
    else :
        if a.count(3) > b.count(3):
            print("A")
        elif a.count(3) < b.count(3):
            print("B")
        else :
            if a.count(2) > b.count(2):
                print("A")
            elif a.count(2) < b.count(2):
                print("B")
            else :
                if a.count(1) > b.count(1):
                    print("A")
                elif a.count(1) < b.count(1):
                    print("B")
                else :
                    print("D")