a,b = map(int, input().split())
c,d = map(int, input().split())
n1 = (a+b-1)%4
n2 = (n1+c+d-1)%4
print(n2+1)