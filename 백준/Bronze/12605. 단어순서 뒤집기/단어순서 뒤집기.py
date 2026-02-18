import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, n+1) :
    lst = list(input().split())
    print(f"Case #{i}: ", end='')
    for j in range(len(lst)-1, -1, -1):
        print(lst[j], end=' ')
    print()