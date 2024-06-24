import sys
num = int(sys.stdin.readline())
lst = []
for i in range(num) :
    w, h = map(int, sys.stdin.readline().split())
    ppi = ((w**2+h**2)**0.5)
    lst.append([i+1, ppi])

lst.sort(key = lambda x : (-x[1], x[0]))
for j in range(num) :
    print(lst[j][0])