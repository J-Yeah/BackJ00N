#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n%4==0) {printf("Even");}
    else if (n%2) {printf("Either");}
    else {printf("Odd");}
    return 0;
}