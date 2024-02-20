import sys

num = int(sys.stdin.readline())
a=list()

for i in range(num) :
    a.append(int(sys.stdin.readline()))

a.sort()

for i in range(len(a)):
    print(a[i])