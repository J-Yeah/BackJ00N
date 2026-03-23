#include <stdio.h>

int main() {
    int t, n, k;
    scanf("%d", &t);
    for (int i=0;i<t;i++){
        scanf("%d %d", &n, &k);
        if (n==1) {
            printf("1\n");
        }
        else if (k!=2){
            printf("-1\n");
        }
        else {
            for (int j=2;j<=n;j++){
                printf("%d ", j);
            }
            printf("1\n");
        }
    }
    return 0;
}