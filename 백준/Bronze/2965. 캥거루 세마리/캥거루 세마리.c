#include <stdio.h>
int main(void){
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    if (b-a-1 > c-b-1) printf("%d", b-a-1);
    else printf("%d", c-b-1);
    return 0;
}