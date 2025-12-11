import sys
input = sys.stdin.readline
d = int(input())
e = int(input())
for i in range(e):
    a = input().strip()
    if a == "+" :
        d += int(input())
    elif a == "-":
        d -= int(input())
print(d)