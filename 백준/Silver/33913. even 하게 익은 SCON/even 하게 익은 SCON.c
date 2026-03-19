#include <stdio.h>

int main() {
    long dp[1000001][2];
    dp[1][0] = 24;
    dp[1][1] = 2;
    long m = 1000000007;
    for (int i = 2;i<1000001;i++){
        dp[i][0] = (dp[i-1][0]*24 + dp[i-1][1]*2)%m;
        dp[i][1] = (dp[i-1][0]*2 + dp[i-1][1]*24)%m;
    }
    int n;
 
    scanf("%d", &n);
    printf("%ld", dp[n][0]);
    return 0;
}