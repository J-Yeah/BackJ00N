#include <stdio.h>

int main(void){
    long int a=0,b=0 ;
    int num;
    scanf("%d", &num);
    
    for(int i=0;i<=num;i++){
        a += i;
    }
    for (int i=0;i<=num;i++){
        b += i*i*i;
    }
    printf("%ld\n%ld\n%ld", a, a*a, b);
    return 0;
}