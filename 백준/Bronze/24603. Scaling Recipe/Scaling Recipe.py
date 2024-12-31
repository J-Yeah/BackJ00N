n, x, y = map(int, input().split())
z = y/x
for i in range(n):
    a = int(input())
    print(round(a*z))