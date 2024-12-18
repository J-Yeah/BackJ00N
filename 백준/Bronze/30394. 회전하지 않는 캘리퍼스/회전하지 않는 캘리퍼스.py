a = list()
for _ in range(int(input())):
    x, y = map(int, input().split())
    a.append(y)
print(max(a)-min(a))