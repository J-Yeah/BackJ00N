#include <stdio.h>

int main() {
    int x, n, p, next = 0;
    scanf("%d", &x);
    scanf("%d", &n);
    next = x;
    for (int i=0;i<n;i++){
        scanf("%d", &p);
        next += x - p;
    }
    printf("%d", next);
    return 0;
}