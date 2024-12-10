import sys
s = list()
n = int(sys.stdin.readline())
for i in range(n):
    a, b = sys.stdin.readline().split()
    s.append([int(a),b])

s.sort(key=lambda x : x[0])
for j in range(n):
    print(s[j][0], s[j][1])