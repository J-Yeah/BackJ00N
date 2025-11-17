a = input()
b = input()
c = ""
for i in range(len(a)):
    c += str(max(int(a[i]), int(b[i])))
print(c)