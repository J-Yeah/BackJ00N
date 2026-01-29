#include <stdio.h>

int main() {
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    char nw[n][100], mw[m][100];
    for (int i=0;i<n;i++){scanf("%s", &nw[i]);}
    for (int j=0;j<m;j++){scanf("%s", &mw[j]);}
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            printf("%s as %s\n", nw[i], mw[j]);
        }
    }
    return 0;
}