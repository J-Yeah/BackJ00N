n = int(input())
while True:
    if n == 1 :
        break
    print(n, end=' ')
    if n%2 == 0 :
        n = int(n/2)
    elif n%2 == 1 :
        n = n*3+1
print(1)