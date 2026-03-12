s = int(input())
d = float(input())
t = float(input())
cnt = s*(5280/3600)*t
if d <= cnt :
    print("MADE IT")
else :
    print("FAILED TEST")