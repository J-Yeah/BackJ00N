#include <stdio.h>
int main() {
    int a,b,c,num;
    scanf("%d %d %d", &a, &b, &c);
    num = (a*b)-c;
    if (num > 0) printf("%d", num);
    else printf("0");
    return 0;
}