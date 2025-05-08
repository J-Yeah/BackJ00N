import sys
input = sys.stdin.readline
p0 = [0]*41
p1 = [0]*41
p0[0] = 1
p1[1] = 1
for i in range(2, 41):
    p0[i] = p0[i-1] + p0[i-2]
    p1[i] = p1[i-1] + p1[i-2]
for _ in range(int(input())):
    n = int(input())
    print(p0[n], p1[n])