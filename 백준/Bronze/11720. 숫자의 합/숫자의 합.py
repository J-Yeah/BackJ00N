import sys

x = int(sys.stdin.readline())
num = list(sys.stdin.readline().rstrip())
total = 0

for i in range(1, x+1):
    total += int(num[i-1])
    
print(total)