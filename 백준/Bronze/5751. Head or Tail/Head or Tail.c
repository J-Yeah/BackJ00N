#include <stdio.h>

int main() {
    int n,m,j,num;
    while (1){
        scanf("%d", &n);
        if (n==0){return 0;}
        m = 0;
        j = 0;
        for (int i=0; i<n ; i++){
            scanf("%d", &num);
            if (num==0){m++;}
            if (num==1){j++;}
        }
        printf("Mary won %d times and John won %d times\n", m,j);
    }
    return 0;
}