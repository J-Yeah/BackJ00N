#include <stdio.h>

int main() {
    int t, total=0;
    scanf("%d", &t);
    t = 1000-t;
    total += t/500;
    t = t%500 ;
    total += t/100;
    t = t%100;
    total += t/50;
    t = t%50;
    total += t/10;
    t = t%10;
    total += t/5;
    t = t%5;
    total += t;
    
    printf("%d", total); 
    return 0;
}