import math
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
a = 0
b = 0 
for i in lst:
    if(i%2==0):
        b+=1
    else:
        a+=1
if a==math.ceil(n/2) and b==n//2 :
    print(1)
else:
    print(0)