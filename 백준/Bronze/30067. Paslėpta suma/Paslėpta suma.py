lst = [int(input()) for _ in range(10)]
sum_lst = sum(lst)

for n in lst :
    if sum_lst - n == n:
        print(n)
        break