#include <stdio.h>
int main(void){
    int a;
    scanf("%d", &a);
    for(int i=1;i<=a;i++){
        printf("%d ", i);
        if (i%6==0 || i==a) printf("Go! ");
    }
    return 0;
}