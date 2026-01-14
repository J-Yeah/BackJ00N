import sys
input = sys.stdin.readline
for _ in range(int(input())):
    cnt = 0
    n = input().strip()
    for i in range(len(n)-2):
        if n[i:i+3] == 'WOW':
            cnt += 1
    print(cnt)