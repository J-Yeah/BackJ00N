a, b, c = map(int, input().split())
c4 = a * (0.229) * (0.324)
a3 = b * (0.297) * (0.42)
a4 = c * (0.21) * (0.297)
print(2*c4 + 2*a3 + a4)