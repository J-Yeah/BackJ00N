a=int(input())

for i in range(1,a+1):
    try:
        b=input()
        print(b[0], end='')
        s = 0
        while True:
            x = b[s]
            s+=1

    except:
        print(b[s-1])
