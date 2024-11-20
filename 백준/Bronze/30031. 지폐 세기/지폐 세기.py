n = int(input())
x = 0
for i in range(n):
    a,b = map(int, input().split())
    if a == 136:
        x += 1000
    elif a == 142:
        x += 5000
    elif a == 148:
        x += 10000
    elif a == 154:
        x += 50000
print(x)