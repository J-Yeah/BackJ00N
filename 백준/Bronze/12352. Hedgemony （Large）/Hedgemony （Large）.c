#include <stdio.h>

int main() {
    int t, n;
    scanf("%d", &t);
    for (int i=1;i<=t;i++){
        scanf("%d", &n);
        
        double h[1001];
        for (int i = 0; i < n; i++) {
            scanf("%lf", &h[i]);
        }

        for (int j = 1; j <= n - 2; j++) {
            double avg = (h[j - 1] + h[j + 1]) / 2.0;
            if (h[j] > avg) {
                h[j] = avg;
            }
        }
        printf("Case #%d: %.6f\n", i, h[n-2]);
    }
    return 0;
}