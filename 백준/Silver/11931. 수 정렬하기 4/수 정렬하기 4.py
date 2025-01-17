import sys
lst = list()
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)
lst.sort(reverse=True)
for j in range(n):
    print(lst[j])