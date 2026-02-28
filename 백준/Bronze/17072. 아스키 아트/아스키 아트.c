#include <stdio.h>

int main() {
    int n,m, r,g,b;
    scanf("%d %d",&n, &m);
    for(int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            int to;
            scanf("%d %d %d",&r, &g, &b);
            to = 2126*r + 7152*g + 722*b;
            if (to<510000) printf("#");
            else if (to<1020000) printf("o");
            else if (to<1530000) printf("+");
            else if (to<2040000) printf("-");
            else printf(".");
        }
        getchar();
        if (i<n-1) printf("\n");
    }
    return 0;
}