mlist = list(map(int, input().split()))
total = 0

for _ in range(int(input())):
    b, l, s = input().split()
    b = int(b)
    l = float(l)
    s = int(s)

    if s >= 17 and l >= 2.0:
        total += mlist[int(b)]

print(total)