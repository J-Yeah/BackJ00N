a = input()
b = a[1:-1]
if a.count('"') >= 2 and b.count('"') == 0 and len(b) :
    print(b)
else :
    print("CE")