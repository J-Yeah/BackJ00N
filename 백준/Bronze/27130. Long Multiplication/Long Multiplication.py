a = input()
b = input()
print(a)
print(b)
for i in range(1, len(b)+1):
    print(int(a)*int(b[-i]))
print(int(a)*int(b))