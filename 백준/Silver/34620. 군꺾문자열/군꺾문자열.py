import sys
a, b = map(int, sys.stdin.readline().split())

if b % 2 == 1:
    print(-1)
else:
    ans = list()
    while True:
        if b%2==1 and b!=1:
            print(-1)
            exit()

        if a < b:
            b //= 2
            ans.append("K")
        else:
            ans.append("G")
            a-=b
            if b==1:
                break

    print(''.join(reversed(ans)))