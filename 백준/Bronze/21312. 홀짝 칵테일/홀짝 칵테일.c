#include <stdio.h>

int main() {
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    int max = 1, hodd = 0;
    if (a%2!=0){
        max *= a;
        hodd = 1;
    }
    if (b%2!=0){
        max *= b;
        hodd = 1;
    }
    if (c%2!=0){
        max *= c;
        hodd = 1;
    }
    if (!hodd){max = a*b*c ;}
    printf("%d", max);
    return 0;
}