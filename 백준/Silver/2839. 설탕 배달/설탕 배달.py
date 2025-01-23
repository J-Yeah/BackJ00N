a = int(input())
i = 0
if a%5 == 0 :
    print(a//5)
else :
    while True:
        a -= 3
        i += 1
        if a%5 == 0 :
            print(i+a//5)
            break
        elif a < 3 :
            print(-1)
            break
        elif a == 0 :
            print(i)
            break