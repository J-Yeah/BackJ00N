a, b = map(int, input().split())
r = 1
for i in range(a, b+1):
    r *= sum([j for j in range(1, i+1)])
print(r%14579)