n = int(input())
for i in range(n):
    print(' '*i, end='')
    print('*'*(2*n-2*i-1))
for j in range(1, n):
    print(' '*(n-j-1), end='')
    print('*'*(2*j+1))