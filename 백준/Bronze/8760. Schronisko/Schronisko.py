import sys
input = sys.stdin.readline
for _ in range(int(input())):
    w,k = map(int, input().split())
    print((w*k)//2)