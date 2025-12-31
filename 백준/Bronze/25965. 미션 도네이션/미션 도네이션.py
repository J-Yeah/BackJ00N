import sys
input = sys.stdin.readline
for i in range(int(input())):
    m = int(input())
    misson_k = list()
    misson_d = list()
    misson_a = list()
    for j in range(m) :
        mk, md, ma = map(int, input().split())
        misson_k.append(mk)
        misson_d.append(md)
        misson_a.append(ma)
    k, d, a = map(int, input().split())
    total = 0
    for x in range(m) :
        total += max(0, misson_k[x]*k - misson_d[x]*d + misson_a[x]*a)
    print(total)