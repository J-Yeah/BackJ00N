num = int(input())

for i in range(1, num+1) :
    a, b = input().split()
    a = int(a)
    n=0
    while n<len(b):
        for j in range(a):
            print(b[n], end='')
        n += 1
    print()
