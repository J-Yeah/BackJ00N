max_n = 0
max_row = 1
max_col = 1
for i in range(9):
    a = list(map(int, input().split()))
    if max(a) > max_n :
        max_n = max(a)
        max_col = i+1
        max_row = a.index(max_n)+1
print(max_n)
print(max_col, max_row)