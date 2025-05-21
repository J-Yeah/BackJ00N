import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*n
    b[m] = 1
    cnt = 0
    while True :
        if a[0] < max(a) :
            a.append(a.pop(0))
            b.append(b.pop(0))
        else :
            cnt += 1
            a.pop(0)
            if b.pop(0) == 1 :
                print(cnt)
                break