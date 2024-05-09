a,b=map(float,input().split())
c = 1000/b*a
num = int(input())

for i in range(num):
    a,b=map(float,input().split())
    if c>1000/b*a :
        c = 1000/b*a

print(round(c,2))