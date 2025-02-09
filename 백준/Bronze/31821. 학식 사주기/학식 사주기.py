import sys
lst = list()
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    lst.append(a)
total = 0
for i in range(int(sys.stdin.readline())):
    b = int(sys.stdin.readline())
    total += lst[b-1]
print(total)