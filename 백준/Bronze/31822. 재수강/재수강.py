scode = input()
n = int(input())
result = 0
 
for _ in range(n):
    acode = input()
    if scode[:5] == acode[:5]:
        result += 1

print(result)