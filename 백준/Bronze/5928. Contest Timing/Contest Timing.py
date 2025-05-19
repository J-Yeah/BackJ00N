d,h,m = map(int, input().split())
d = d - 11
h = h - 11 + 24*d
m = m - 11 + 60*h
print(max(-1,m))