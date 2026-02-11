#include <stdio.h>

int main() {
    float d, w, fi = 3.14159, a;
    int n;
    scanf("%f", &d);
    scanf("%f", &w);
    scanf("%d", &n);
    a = d*fi/w;
    if (a>n) {printf("YES");}
    else {printf("NO");}
    return 0;
}