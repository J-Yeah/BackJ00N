#include <stdio.h>


int main() {
    int cu, du, cd, dd, cp, dp, h;
    scanf("%d %d", &cu, &du);
    scanf("%d %d", &cd, &dd);
    scanf("%d %d", &cp, &dp);
    scanf("%d", &h);

    int i = 0;
    h -= (du+dd+dp);
    while (1){
        if (h<=0) break;
        i++;
        if (i%cu == 0) h -= du;
        if (i%cd == 0) h -= dd;
        if (i%cp == 0) h -= dp;
    }
	printf("%d", i);

    return 0;
}