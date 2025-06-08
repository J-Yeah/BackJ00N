import sys
for _ in range(int(input())):
    lst = input().strip()
    m,n,o = map(int, lst.split())
    for i in range(o):
        m,n = int(max(m,n)/2), min(m,n)
    print("Data set:", lst)
    print(max(m,n), min(m,n))
    print()