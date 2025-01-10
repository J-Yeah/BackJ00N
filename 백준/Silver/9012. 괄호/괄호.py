import sys
for _ in range(int(sys.stdin.readline())):
    lst1 = list(sys.stdin.readline().strip())
    n = len(lst1)
    lst2 = list(lst1)
    lst2.reverse()
    for i in range(n):
        try :
            if lst1.count('(') + lst1.count(')') == 0 :
                print("YES")
                break
            a = len(lst1) - 1 - lst2.index('(')
            b = lst1.index(')', a)
            rb = len(lst1) - 1 - b
            lst1.pop(a)
            lst1.pop(b-1)
            lst2.remove('(')
            lst2.pop(rb)
        except :
            print("NO")
            break