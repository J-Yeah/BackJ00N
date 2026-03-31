import sys
input = sys.stdin.readline

t = int(input())

for x in range(1, t+1):
    a, b, k = map(int, input().split())
    ans = 0

    for i in range(a):
        for j in range(b):
            if (i & j) < k:
                ans += 1

    print(f"Case #{x}: {ans}")