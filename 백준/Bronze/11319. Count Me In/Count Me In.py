import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = list(input().split())
    b = ""
    for i in range(len(a)):
        b += a[i]
    b = b.lower()
    c = b.count('a')+b.count('e')+b.count('i')+b.count('o')+b.count('u')
    print(len(b)-c, c)