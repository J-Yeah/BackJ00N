import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break

    d = 0
    time = 0
    for _ in range(n):
        s, t = map(int, input().split())
        d += s*(t-time)
        time = t
    print(d, "miles")