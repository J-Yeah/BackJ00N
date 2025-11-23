import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = input().strip()
    print(a[0].upper() + a[1:])