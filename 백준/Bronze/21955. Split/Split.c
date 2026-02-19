#include <stdio.h>
#include <string.h>

int main() {
    char n[25];
    scanf("%s", n);
    int len = strlen(n)/2;
    char *first = n;
    char *second = &n[len];

    printf("%.*s %s", len, first, second); 
    return 0;
}