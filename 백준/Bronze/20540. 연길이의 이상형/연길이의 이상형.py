s = input()
lis = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
for i in s:
    lis.remove(i)
res = ''.join(lis)
print(res)