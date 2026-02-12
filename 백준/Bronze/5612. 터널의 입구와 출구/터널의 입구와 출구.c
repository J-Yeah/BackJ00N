#include <stdio.h>

int main() {
    int n, m, incar, outcar, maxcar;
    scanf("%d", &n);
    scanf("%d", &m);
    maxcar = m;
    for (int i=0;i<n;i++){
        scanf("%d %d", &incar, &outcar);
        m = m + incar - outcar ;
        if (m > maxcar) {maxcar = m;}
        if (m < 0) {
            printf("0");
            return 0;
        }
    }
    printf("%d", maxcar);
    return 0;
}