n, m, a, b = map(int, input().split())
x = 0
if n * 3 - m > 0:
    x = (n * 3 - m) * a + b
print(x)