a = int(input())
b = int(input())
total = 0
    
for i in range(1, b+1):
    c,d=input().split()
    c = int(c)
    d = int(d)
    total += c*d
    
if a==total :
    print("Yes")
else:
    print("No")