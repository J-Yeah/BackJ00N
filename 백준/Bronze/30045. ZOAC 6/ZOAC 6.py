import sys
n = int(sys.stdin.readline())
s = 0
for i in range(n):
    a = sys.stdin.readline()
    if a.count('01') + a.count('OI') :
        s += 1
print(s)