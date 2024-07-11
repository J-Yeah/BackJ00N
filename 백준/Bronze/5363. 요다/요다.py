import sys
num = int(sys.stdin.readline())
for i in range(num):
    lst = list(sys.stdin.readline().split())
    for j in range(len(lst)-2):
        print(lst[j+2], end=' ')
    print(lst[0], lst[1])