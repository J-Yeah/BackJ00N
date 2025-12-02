n = int(input())
if n>=1000000 :
    a = 0.2
elif n>=500000 :
    a = 0.15
elif n>=100000 :
    a = 0.1
else :
    a = 0.05
print(int(n*a), int(n*(1-a)))