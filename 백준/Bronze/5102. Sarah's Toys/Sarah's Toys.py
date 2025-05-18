import sys
input = sys.stdin.readline
while True:
    a,b = map(int, input().split())
    if a==0 and b==0 :
        break
    x = (a-b)
    if x>3 :
        print(x//2-x%2, x%2)
    elif x==3 :
        print(0, 1)
    elif x==2 :
        print(1, 0)
    else :
        print(0, 0)