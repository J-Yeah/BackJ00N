#include <stdio.h>
int main(void){
    int a,b,c,d,e,f,g;
    scanf("%d %d %d %d\n%d %d %d", &a, &b, &c, &d, &e, &f, &g);
    if (a==e) printf("1");
    else if (b==e) printf("2");
    else if (c==e) printf("3");
    else if (d==e) printf("4");
    else printf("0");
    return 0;
}