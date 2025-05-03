import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    parts = input().split()
    cmd = parts[0]
    
    if cmd == "add":
        s.add(int(parts[1]))
    elif cmd == "remove":
        s.discard(int(parts[1]))
    elif cmd == "check":
        if int(parts[1]) in s :
            print(1)
        else :
            print(0)
    elif cmd == "toggle":
        x = int(parts[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif cmd == "all":
        s = set(range(1, 21))
    elif cmd == "empty":
        s.clear()