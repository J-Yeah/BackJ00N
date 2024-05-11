#include <stdio.h>
int main(void){
    int a,b,c,d, max;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    max = a;
    int num[] = {a,b,c-a,d-b};
    for (int i=0;i<4;i++){
        if (max>num[i]) max=num[i];
    }
    printf("%d", max);
    return 0;
}