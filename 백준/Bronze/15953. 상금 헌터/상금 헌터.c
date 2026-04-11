#include <stdio.h>

int main() {
    int t, n, m, total;
    scanf("%d", &t);
    
    for (int i=0;i<t;i++){
        total = 0;
        scanf("%d %d", &n, &m);
        if (n<=21 && n>0) {
            if (n==1) total += 5000000;
            else if (n>=2 && n<=3) total += 3000000;
            else if (n>=4 && n<=6) total += 2000000;
            else if (n>=7 && n<=10) total += 500000;
            else if (n>=11 && n<=15) total += 300000;
            else if (n>=16 && n<=21) total += 100000;
        }
        if (m<=31 && m>0) {
            if (m==1) total += 5120000;
            else if (m>=2 && m<=3) total += 2560000;
            else if (m>=4 && m<=7) total += 1280000;
            else if (m>=8 && m<=15) total += 640000;
            else if (m>=16 && m<=31) total += 320000;
        }
        printf("%d\n", total);
    }
    return 0;
}