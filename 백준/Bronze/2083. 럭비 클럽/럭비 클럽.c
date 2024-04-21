#include <stdio.h>

int main(void){
    while(1){
        char name[11];
        int a,b;
        
        scanf("%s %d %d", name, &a, &b);
        if ((a==0)&&(b==0)) break;
        if ((a>17)||(b>=80)) printf("%s Senior\n", name);
        else printf("%s Junior\n", name);
    }
    return 0;
}