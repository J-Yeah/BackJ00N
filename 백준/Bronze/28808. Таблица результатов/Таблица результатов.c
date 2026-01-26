#include <stdio.h>
#include <stdbool.h>

int main() {
    int n,m, total;
    total = 0;
    char c;
    scanf("%d %d", &n, &m);
    for (int i=0;i<n;i++){
        bool correct=false;
        for (int j=0;j<m;j++){
            c = getchar();
            if (c =='+') {correct=true;}
        }
        if (correct) {total++;}
        c = getchar();
    }
    printf("%d", total);
    return 0;
}