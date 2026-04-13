#include <stdio.h>
#include <math.h>

int main() {
    int t, n;
    long long a, b;
    scanf("%d", &t);
    
    for (int i = 0;i<t;i++){
        scanf("%d %lld %lld", &n, &a, &b);
        long long x = (1ll << n)^a^b;
        int cnt = 0;
        while (x) {
            x &= (x - 1);
            cnt++;
        }
        printf("%d\n", cnt);
    }
    return 0;
}