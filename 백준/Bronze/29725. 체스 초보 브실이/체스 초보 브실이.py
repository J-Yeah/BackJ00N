a = input()
for i in range(7):
    a += input()
b = a.count('p')*1 + a.count('n')*3 + a.count('b')*3 + a.count('r')*5 + a.count('q')*9
c = a.count('P')*1 + a.count('N')*3 + a.count('B')*3 + a.count('R')*5 + a.count('Q')*9
print(c-b)