a = int(input())
if a > 0 :
    b = 1
else :
    b = 0

if abs(a) <= 2**15 - b :
    print("short")
elif abs(a) <= 2**31 - b :
    print("int")
else :
    print("long long")