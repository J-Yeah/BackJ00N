n = int(input())
a = input()
s = 0

for i in range(n):
    s += (ord(a[i])-96)*(31**i)

print(s)