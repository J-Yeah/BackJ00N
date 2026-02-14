#include <stdio.h>

int main() {
    int n, a, c, total=0;
    scanf("%d %d", &n, &a);
    for (int i=0 ;i<n;i++){
        scanf("%d", &c);
        total += c/a;
    }
    printf("%d", total);
    return 0;
}