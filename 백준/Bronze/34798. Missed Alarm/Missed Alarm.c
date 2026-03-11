#include <stdio.h>
#include <math.h>

int main() {
    int ah,am, h, m;
    scanf("%d:%d", &ah, &am);
    scanf("%d:%d", &h, &m);
    h = ah-h;
    m = am-m + h*60;
    if (m<0) printf("YES");
    else printf("NO");
    return 0;
}