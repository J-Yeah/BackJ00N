#include <stdio.h>

int main() {
    int t, n, num, total;
    scanf("%d", &t);
    for (int j=0;j<t;j++){
        total = 0;
        scanf("%d", &n);
        for (int i=0; i<n ; i++){
            scanf("%d", &num);
            total = total+num;
        }
        printf("%d\n", total);
    }
    return 0;
}