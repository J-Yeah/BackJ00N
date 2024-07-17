a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

bm = max(abs(e-a), abs(f-b))
dm = abs(e-c) + abs(f-d)

if bm < dm:
    print("bessie")
elif bm > dm:
    print("daisy")
else:
    print("tie")