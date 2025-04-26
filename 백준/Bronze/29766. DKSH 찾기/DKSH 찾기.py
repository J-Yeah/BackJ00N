a = input()
result = 0

for i in range(len(a)-3):
    if a[i:i+4] == "DKSH":
        result += 1

print(result)