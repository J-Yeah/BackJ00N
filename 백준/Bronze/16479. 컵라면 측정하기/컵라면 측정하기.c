#include <stdio.h>

int main() {
    int k;
    double d1, d2, h;
    scanf("%d", &k);
    scanf("%lf %lf", &d1, &d2);
    h = k*k - ((d1-d2)/2)*((d1-d2)/2);
    printf("%f", h);
    return 0;
}