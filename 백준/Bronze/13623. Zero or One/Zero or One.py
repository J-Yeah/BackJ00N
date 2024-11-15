lst = list(input().split())
a = "ABC"
if lst.count('1') == 1 :
    print(a[lst.index('1')])
elif lst.count('1') == 2 :
    print(a[lst.index("0")])
else :
    print("*")