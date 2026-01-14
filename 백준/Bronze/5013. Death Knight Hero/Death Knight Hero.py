import sys
input = sys.stdin.readline
total = 0
for i in range(int(input())):
    a = input().strip()
    if not 'CD' in a :
        total += 1
print(total)