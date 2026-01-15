a, b = map(int, input().split())
ns = abs((a-1)//4 - (b-1)//4)
ew = abs((a-1)%4 - (b-1)%4)
print(ns+ew)