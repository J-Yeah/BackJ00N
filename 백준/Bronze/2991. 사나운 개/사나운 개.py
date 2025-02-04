def cnt(x, y, z) :
    u = x % (y+z)
    if u <= y and u != 0 :
        return 1
    else :
        return 0
    
a,b,c,d = map(int, input().split())
p,m,n = map(int, input().split())

print(cnt(p,a,b)+cnt(p,c,d))
print(cnt(m,a,b)+cnt(m,c,d))
print(cnt(n,a,b)+cnt(n,c,d))