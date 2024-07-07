n, m = map(int, input().split())
book = 0
box = 0
if n != 0 :
    lst = list(map(int, input().split()))
    box += 1
    for i in range(n) :
        book += lst[i]
        if book > m :
            book = lst[i]
            box += 1
print(box)