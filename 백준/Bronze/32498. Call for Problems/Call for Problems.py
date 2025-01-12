import sys
lst = list()
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline()) % 2
    lst.append(a)
print(lst.count(1))