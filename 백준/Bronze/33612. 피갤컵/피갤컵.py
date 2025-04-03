n = int(input())
m = (1 + n*7) % 12
y = 2024 + (1+n*7)//12
if m == 0 :
    m = 12
    y -= 1
print(y,m)