a = input()
b = input()
x1 = ord(a[0]) - ord('a') + 1
x2 = ord(b[0]) - ord('a') + 1
x = abs(x1-x2)
y = abs(int(a[1])-int(b[1]))
print(min(x,y), max(x,y))