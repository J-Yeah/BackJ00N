import sys
import math

b = list()
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline()
    a = int(a.replace('0', '9').replace('6', '9'))
    if a > 100 :
        a = 100
    b.append(int(a))

c = sum(b)/len(b)
if c - int(c) >=0.5 : print(math.ceil(c))
else: print(math.floor(c))