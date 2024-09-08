import sys

num = int(sys.stdin.readline())
total = 0
for i in range(num) :
    a = sys.stdin.readline()
    b = a.split('-')
    c = int(b[1])
    if c <=90:
        total += 1
print(total)