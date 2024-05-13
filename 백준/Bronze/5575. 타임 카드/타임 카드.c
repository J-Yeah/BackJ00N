#include <stdio.h>
int main(void){
    int a,b,c,d,e,f,num_h,num_m,num_s ;
    for (int i=0;i<3;i++){
        scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
        num_h = d-a ;
        num_m = e-b ;
        num_s = f-c ;
        if (num_s<0){
            num_s += 60;
            num_m -= 1;
        }
        if (num_m<0){
            num_m += 60;
            num_h -= 1;
        }
        printf("%d %d %d\n", num_h, num_m, num_s);
    }
    return 0;
}