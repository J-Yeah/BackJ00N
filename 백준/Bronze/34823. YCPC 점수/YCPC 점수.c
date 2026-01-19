#include <stdio.h>

int main() {
    int y, c, p, min;
    scanf("%d %d %d", &y, &c, &p);
    min = y;
    if (min>c/2){min = c/2;}
    if (min>p){min = p;}
    printf("%d", min);
}