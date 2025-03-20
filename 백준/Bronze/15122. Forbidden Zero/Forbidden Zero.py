a = int(input())
while True:
    a += 1
    b = str(a)
    if b.count('0') == 0:
        break
print(a)