import sys
input = sys.stdin.readline

a = input().strip()

lst = list(a.split('-'))
a_list = list(map(int, lst[0].split('+')))
total = sum(a_list)
for i in range(1, len(lst)):
    total -= sum(list(map(int, lst[i].split('+'))))
print(total)