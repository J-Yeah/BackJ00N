#include <stdio.h>
int main(void){
    int a,b,c,d,e,f,g,h,to1,to2;
    scanf("%d %d %d %d\n%d %d %d %d", &a, &b, &c, &d, &e, &f, &g, &h);
    to1 = a+b+c+d ;
    to2 = e+f+g+h ;
    if (to1<to2) printf("%d", to2);
    else printf("%d", to1);
    return 0;
}