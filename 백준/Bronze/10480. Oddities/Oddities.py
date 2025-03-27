import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = int(input())
    if a % 2 :
        print(a,"is odd")
    else :
        print(a,"is even")