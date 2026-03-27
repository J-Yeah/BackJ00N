#include <stdio.h>
#include <math.h>

int main() {
    int n;
    double p, q;
    
    double q_dp[21];
    double p_dp[21][21];

    scanf("%d", &n);
    scanf("%lf %lf", &p, &q);

    q_dp[0] = pow(1-q, n);
    for (int i = 1; i <= n; i++) q_dp[i] = q_dp[i -1] * (n - i + 1) / i * (q / (1-q));

    for (int i = 0; i <= n; i++) {
        p_dp[i][0] = pow(1-p, i);
        for (int j = 1; j <= i; j++) p_dp[i][j] = p_dp[i][j-1] * (i-j+1) / j * (p / (1-p));
    }

    double max_v = 0.0;
    for (int i = 0; i <= n; i++) {
        double total_ex = 0.0;
        for (int j = 0; j <= i; j++) {
            double total = 0.0;
            for (int x = 0; x <= n - j; x++) total += (x + j) * q_dp[x] * p_dp[i][j];
            total_ex += total;
        }
        if (i == 0 || total_ex > max_v)
            max_v = total_ex;
    }

    printf("%.10lf", max_v);

    return 0;
}