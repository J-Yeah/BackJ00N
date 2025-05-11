import sys
input = sys.stdin.readline
lst = list()
for _ in range(int(input())):
    a = int(input())
    if a == 0 :
        lst.pop()
    else :
        lst.append(a)
print(sum(lst))