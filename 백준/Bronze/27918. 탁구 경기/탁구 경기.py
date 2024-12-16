d = 0
p = 0
for _ in range(int(input())):
    n = input()
    if n == 'D' :
        d += 1
    elif n == 'P' :
        p += 1
    if abs(d-p) >= 2 :
        break
print(f"{d}:{p}")