#include <stdio.h>
#include <string.h>

int main() {
    long int ah=0,bh=0;
    char a[1000001], b[1000001];
    scanf("%s %s", a, b);
    for (int i=0;i<strlen(a);i++){
        int n = a[i]-'0';
        ah += n;
    }
    for (int i=0;i<strlen(b);i++){
        int n = b[i]-'0';
        bh += n;
    }
    if (ah*strlen(a) > bh*strlen(b)) printf("1");
    else if (ah*strlen(a) < bh*strlen(b)) printf("2");
    else printf("0");
    return 0;
}