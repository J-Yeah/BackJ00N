n = int(input())
s = 1
while True :
    if s+s*s == n-1 :
        print(s)
        break
    s += 1