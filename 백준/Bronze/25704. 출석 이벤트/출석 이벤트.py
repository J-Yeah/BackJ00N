a = 0
b = 1
c = 0
d = 1

n = int(input())
p = int(input())

if n >= 5 :
    a = 500
if n >= 10 :
    b = 0.9
if n >= 15 :
    c = 2000
if n >= 20 :
    d = 0.75

print(min(max(0,p-a),round(p*b),max(0,p-c),round(p*d)))