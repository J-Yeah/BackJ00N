n = int(input())
a = input()
b = input()

n1 = True
n2 = False
n3 = False

lst = 'abcdefghijklmnopqrstuvwxyz'
for i in lst :
    if a.count(i) != b.count(i) :
        n1 = False
        break

if a[0] == b[0] and a[n-1] == b[n-1] :
    n2 = True

a = a.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
b = b.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')

if a == b :
    n3 = True

if n1 and n2 and n3 :
    print("YES")
else :
    print("NO")