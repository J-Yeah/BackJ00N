n = int(input())
a = input()
m = 0
for i in range(n//2):
    if a[i] != a[-i-1] :
        m += 1
print(m)