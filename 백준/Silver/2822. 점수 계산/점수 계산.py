lst = list()
for i in range(1, 9):
    a = int(input())
    b = [i,a]
    lst.append(b)
lst.sort(key = lambda x: x[1])
lst2 = lst[3:8]
lst2.sort(key = lambda x: x[0])

print(lst2[0][1]+lst2[1][1]+lst2[2][1]+lst2[3][1]+lst2[4][1])
print(lst2[0][0], lst2[1][0], lst2[2][0], lst2[3][0], lst2[4][0])