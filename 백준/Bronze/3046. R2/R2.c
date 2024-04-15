#include <stdio.h>

int main(void){
    int a, b;
    scanf("%d %d", &a, &b);
    
    b = b*2 - a;
    printf("%d", b);
    
    return 0;
}