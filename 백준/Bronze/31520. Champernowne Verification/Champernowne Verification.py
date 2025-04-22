a = input()
x = 1
for i in range(1,len(a)):
    if int(a[0])==1 and int(a[i-1]) + 1 == int(a[i]) :
        x += 1
    else :
        x -= 100
if x > 0 :
    print(x)
else :
    print(-1)