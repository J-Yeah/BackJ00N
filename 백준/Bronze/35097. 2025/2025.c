#include <stdio.h>

int main() {
    while (1){
        int a, sum=0;
        scanf("%d", &a);
        if (a==0) return 0;
        for (int i = 1; i <= a; i++) {
                for (int j = 1; j <= a; j++) {
                    sum += i * j;
                }
        }
        printf("%d\n", sum);
    }
    return 0;
}