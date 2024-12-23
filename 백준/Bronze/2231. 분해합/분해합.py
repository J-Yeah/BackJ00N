n = int(input())
s = True
for i in range(n):
    a = str(i)
    if i+sum(int(digit) for digit in a) == n :
        print(i)
        s = False
        break

if s :
    print(0)