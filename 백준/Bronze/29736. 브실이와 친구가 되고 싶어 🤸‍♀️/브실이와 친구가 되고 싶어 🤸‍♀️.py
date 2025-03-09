a,b = map(int, input().split())
k,x = map(int, input().split())
z = max(0, min(b, k+x) - max(a, k-x) + 1)
if z :
    print(z)
else :
    print("IMPOSSIBLE")