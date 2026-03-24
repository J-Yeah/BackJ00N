#include <stdio.h>

int main() {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);

    if (m==n || k>=m) {
        printf("-1");
        return 0;
    }

    for (int i = 1; i < k; i++) printf("%d ", i);
    for (int i = n; i > m ; i--) printf("%d ", i);
    for (int i = k; i <= m; i++) printf("%d ", i);

    return 0;
}