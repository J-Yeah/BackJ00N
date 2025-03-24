k,w,m = map(int, input().split())
print((w-k)//m + min(1, (w-k)%m))