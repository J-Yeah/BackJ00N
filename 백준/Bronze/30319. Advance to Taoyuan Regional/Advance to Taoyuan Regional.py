y,m,d = map(int, input().split('-'))
total = m*30 + d
s = 10*30 + 21 - 35
if s >= total :
    print("GOOD")
else :
    print("TOO LATE")