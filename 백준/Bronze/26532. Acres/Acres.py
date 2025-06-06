x,y = map(int,input().split())
z = x*y
a = 5*4840
print(z//a + min(1,z%a))