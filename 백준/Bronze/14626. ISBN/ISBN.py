a = input()
s = 0
for i in range(len(a)) :
    if a[i] == '*' :
        m = i+1
    elif i%2 == 0 :
        s += int(a[i])
    elif i%2 != 0 :
        s += int(a[i])*3
if m%2 == 0 :
    for i in range(10):
        if (s+(i*3)) % 10 == 0:
            print(i)
            break
else :
    print(10 - s%10)