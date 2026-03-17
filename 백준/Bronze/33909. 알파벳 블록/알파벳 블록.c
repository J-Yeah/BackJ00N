#include <stdio.h>

int main() {
    int s,c,o,n;
    scanf("%d %d %d %d", &s, &c, &o, &n);
    c += o*2;
    n += s;
    if (n/3 < c/6) printf("%d", n/3);
    else printf("%d", c/6);
    return 0;
}