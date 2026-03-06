#include <stdio.h>
#include <string.h>

int main() {
    int n, cnt=0;
    scanf("%d", &n);
    char a[n+1], b[n+1];
    scanf("%s", a);
    scanf("%s", b);
    for (int i=0;i<n;i++){
        if (a[i] == b[i]) cnt++;
    }
    printf("%d", cnt);
    return 0;
}