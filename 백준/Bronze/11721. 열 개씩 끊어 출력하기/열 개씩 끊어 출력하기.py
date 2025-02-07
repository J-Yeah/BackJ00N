a = input()
for i in range(len(a)) :
    if i%10 == 9 :
        print(a[i])
    else :
        print(a[i], end='')