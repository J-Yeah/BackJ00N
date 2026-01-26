#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, ns=0, we=0;
    char d;
    scanf("%d", &n);
    d = getchar();
    for (int i=0;i<n;i++){
        d = getchar();
        if (d=='N') {ns++;}
        if (d=='S') {ns--;}
        if (d=='W') {we++;}
        if (d=='E') {we--;}
    }
    printf("%d", abs(ns)+abs(we));
    return 0;
}