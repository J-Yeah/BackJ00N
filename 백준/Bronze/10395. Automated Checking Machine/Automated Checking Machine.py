a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0
for i in range(len(a)):
    if a[i]==b[i] :
        c = 1
        break
if c == 1 :
    print("N")
else :
    print("Y")