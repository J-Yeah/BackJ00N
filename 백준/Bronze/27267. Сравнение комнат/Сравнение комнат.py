a,b,c,d = map(int, input().split())
n1 = a*b
n2 = c*d
if n1>n2 :
    print("M")
elif n1<n2:
    print("P")
else :
    print("E")