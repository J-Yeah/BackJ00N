import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
ticket = min(lst) - int(max(lst)/2)
if ticket < 0 :
    print(0)
else :
    print(ticket)