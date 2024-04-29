a =[]
b =[]

for i in range(4):
    a.append(int(input()))
for i in range(2):
    b.append(int(input()))
    
a.sort(reverse=True)
b.sort(reverse=True)
print(sum(a[:3])+b[0])
