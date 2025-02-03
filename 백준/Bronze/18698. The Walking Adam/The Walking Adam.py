import sys
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip()
    b = a.find('D')
    if b < 0 :
        print(len(a))
    else :
        print(b)