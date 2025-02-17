result = list()
for _ in range(7):
    a,b = input().split()
    result.append([a, int(b)])

result.sort(key=lambda x : -x[1])
print(result[0][0])