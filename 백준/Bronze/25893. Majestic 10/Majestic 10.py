import sys
input = sys.stdin.readline
x = ['zilch', 'double', 'double-double', 'triple-double']
for _ in range(int(input())):
    a = input().strip()
    b = list(map(int, a.split()))
    c = 0
    for i in b:
        if i%10 == 0 and i != 0 :
            c += 1
    print(a)
    print(x[c])
    print()