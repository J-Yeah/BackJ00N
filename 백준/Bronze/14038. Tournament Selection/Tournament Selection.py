lst = list()
for _ in range(6):
    a = input()
    lst.append(a)
n = lst.count('W')
if n==5 or n==6:
    print(1)
elif n==3 or n==4:
    print(2)
elif n==1 or n==2:
    print(3)
else :
    print(-1)