import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b = map(int, input().split())
    b = b%4+4
    c = (a**b)%10
    if c == 0 :
        c = 10
    print(c)