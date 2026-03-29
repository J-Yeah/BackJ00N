import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    wears = {}
    for j in range(n):
        wear, w_type = list(input().split())
        if w_type in wears:
            wears[w_type].append(wear)
        else:
            wears[w_type] = [wear]

    ans = 1
    for i in wears:
        ans *= (len(wears[i])+1)
    print(ans-1)