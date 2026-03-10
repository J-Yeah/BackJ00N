#include <stdio.h>
#include <math.h>

int main() {
    while (1){
        int a,b,c;
        scanf("%d %d %d", &a, &b, &c);
        if (a==0 && b==0 && c==0) return 0;
        if (a==b && a==c) printf("Equilateral\n");
        else if (a+b<=c || a+c<=b || b+c<=a) printf("Invalid\n");
        else if (a==b || a==c || b==c) printf("Isosceles\n");
        else printf("Scalene\n");
    }
}