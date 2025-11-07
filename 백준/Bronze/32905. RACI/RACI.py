n, m = map(int, input().split())
a = True

for _ in range(n):
    line = list(input().split())
    if line.count("A") != 1:
        a = False

if a :
    print("Yes")
else:
    print("No")