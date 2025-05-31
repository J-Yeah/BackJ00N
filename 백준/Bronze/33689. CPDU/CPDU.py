import sys
input = sys.stdin.readline
cnt = 0
for _ in range(int(input())):
    a = input()
    if a[0]=='C' :
        cnt += 1
print(cnt)