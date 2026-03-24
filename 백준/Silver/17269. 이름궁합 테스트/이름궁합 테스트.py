key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
val = '32124313113132122212111221'

n, m = map(int, input().split())
a, b = input().split()
x = ""

for i in range(max(n,m)):
    try:
        x += a[i]
    except :
        pass
    try:
        x += b[i]
    except:
        pass

y = x.translate(str.maketrans(key, val))

while True :
    if len(y)==2 or len(y) == 1 :
        break
    z = ""
    for j in range(len(y)-1):
        z += str((int(y[j])+int(y[j+1]))%10)
    y = z

print(f"{int(y)}%")