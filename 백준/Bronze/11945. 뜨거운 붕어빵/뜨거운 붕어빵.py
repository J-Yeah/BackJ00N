a,b = map(int, input().split())

for i in range(a):
    s = input()
    for j in range(1,b+1) :
        print(s[-j], end='')
    print()