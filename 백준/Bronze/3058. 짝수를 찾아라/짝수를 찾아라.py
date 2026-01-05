import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    lst2 = list()
    for j in lst:
        if j%2 == 0 :
            lst2.append(j)
    print(sum(lst2), min(lst2))