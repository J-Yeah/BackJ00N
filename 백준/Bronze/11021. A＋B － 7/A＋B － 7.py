import sys

a = int(input())
num = 1

while num<=a :
    b,c = map(int,sys.stdin.readline().split())
    print("Case #%s:"%num,b+c)
    num += 1

