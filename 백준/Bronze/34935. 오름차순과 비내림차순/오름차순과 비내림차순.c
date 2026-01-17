#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int a = 1;
    
    long long prev, cur;
    scanf("%lld", &prev);
    for (int i = 1; i < n; i++) {
        scanf("%lld", &cur);
        if (prev >= cur) {
            a = 0;
            break;
        }
        prev = cur;
    }

    printf("%d", a);
    return 0;
}