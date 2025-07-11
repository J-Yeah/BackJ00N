import sys
input = sys.stdin.readline
n = int(input())
lst = list()
for _ in range(n):
    a = input().strip()
    b = input().strip()
    lst.append([b,a])
for i in range(n):
    print(f"Case {i+1}: {lst[i][0]}, {lst[i][1]}")