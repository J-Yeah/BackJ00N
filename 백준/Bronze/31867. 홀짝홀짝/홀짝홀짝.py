n = int(input())
a = input()
od = 0
ev = 0
for i in a :
    if int(i)%2 == 0 :
        ev += 1
    else :
        od += 1
if ev > od :
    print(0)
elif od > ev :
    print(1)
else :
    print(-1)