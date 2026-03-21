import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = list(map(int, input().split()))


dic = {}

for i in range(len(a)):
    dic[a[i]] = i


cw = 0
ccw = 0
for i in range(1, m):
    now_time = (cw-dic[i]-1)//n+1
    cw = now_time*n+dic[i]+1

for j in range(n, m-1, -1):
    now_time = (ccw-dic[j]-1)//n+1
    ccw = now_time*n+dic[j]+1

if cw > ccw:
    print("CCW")
elif cw < ccw:
    print("CW")
else:
    print("EQ")