import sys
input = sys.stdin.readline
dp = [0]*46
dp[0] = 1
dp[1] = 1
for i in range(2,46) :
    dp[i] = dp[i-1] + dp[i-2]
for _ in range(int(input())):
    print(dp[int(input())])