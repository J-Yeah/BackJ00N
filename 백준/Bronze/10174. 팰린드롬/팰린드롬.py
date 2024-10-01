import sys
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip()
    a = a.lower()
    b = ""
    for i in a:
        b = i+b
    if a==b :
        print("Yes")
    else :
        print("No")