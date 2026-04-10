#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i=1;i<=n*m;i++){
        printf("%d", i);
        if (i%m==0) printf("\n");
        else printf(" ");
    }
    return 0;
}