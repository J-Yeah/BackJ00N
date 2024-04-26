su =0
sumax =0

for i in range(4):
    a,b=map(int,input().split())
    su -= a
    su += b
    if su>sumax :
        sumax = su

print(sumax)
