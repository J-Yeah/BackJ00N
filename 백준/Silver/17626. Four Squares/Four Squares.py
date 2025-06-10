import math

n = int(input())
dp = [0]*(n+1)
dp[1] = 1

for i in range(2, n+1):
    m = i
    for j in range(1, int(math.sqrt(i))+1) :
        m = min(m, dp[i-j*j]+1)
    dp[i] = m

print(dp[n])