import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = 0
    for i in range(int(input())):
        a,b,c = map(str, input().split())
        s += (float(b)*float(c))
    print(f"${s:.2f}")