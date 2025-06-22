import sys
input = sys.stdin.readline
dp = [[1]*30 for _ in range(30)]
for x in range(1,30):
    dp[1][x] = x
for i in range(2,30):
    for j in range(i+1,30):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        
for _ in range(int(input())):
    n,m = map(int, input().split())
    print(dp[n][m])