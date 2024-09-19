n = int(input())
for i in range(n):
    a = input()
    wd = ""
    for p in a :
        wd = wd + chr((ord(p) - 65 + 1) % 26 + 65)
    print(f"String #{i+1}")
    print(wd)
    print()