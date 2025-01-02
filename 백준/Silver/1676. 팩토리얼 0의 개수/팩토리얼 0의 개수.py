import math
a = int(input())
s = math.factorial(a)
b = str(s)
c = 0
for i in range(1, len(b)+1):
    if b[-i] == '0' :
        c += 1
    else :
        break
print(c)