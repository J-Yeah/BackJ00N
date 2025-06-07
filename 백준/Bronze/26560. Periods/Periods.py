import sys
input = sys.stdin.readline
for i in range(int(input())):
    a = input().strip()
    if a[-1] != '.' :
        a = a+'.'
    print(a)