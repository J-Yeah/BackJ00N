import sys
input = sys.stdin.readline

while True :
    try:
        cnt = 0
        n, m = map(int, input().split())
        for i in range(n, m+1):
            s = str(i)
            if len(s) == len(set(s)):
                cnt += 1
        print(cnt)
    except:
        break