s = int(input())
a = int(input())
b = int(input())
r = 250
if s > a :
    r += 100*((s-a)//b + [1, 0][(s - a) % b == 0])
print(r)