a,b = map(int, input().split())
x = a*b

while (b>0) :
    a,b = b, a%b

print(a)
print(x//a)