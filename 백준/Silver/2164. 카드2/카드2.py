import math

a = int(input())
b = 2 ** math.floor(math.log2(a))
c = 2*(a-b)
if c != 0 :
    print(c)
else :
    print(a)