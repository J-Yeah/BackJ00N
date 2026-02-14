#include <stdio.h>

int main() {
    int x, total=0;
    scanf("%d", &x);
    total += 3*(x/2)-2*(x/2);
    if (x%2) {total+=3;}
    printf("%d", total);
    return 0;
}