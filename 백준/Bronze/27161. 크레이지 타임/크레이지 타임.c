#include <stdio.h>
#include <string.h>

int main() {
    int x, n, ti = 12, t = 1;
    char s[10], *ac;
    scanf("%d", &x);
    for (int i=0;i<x;i++){
        scanf("%s %d\n", s, &n);
        ti=(ti+t+12)%12;
        if (ti==0) ti = 12;
        ac = "NO";
        if (ti!=n || strcmp(s, "HOURGLASS") != 0){
            if (ti==n) ac = "YES";
            if (strcmp(s, "HOURGLASS") == 0){
                if (t<0) t = 1;
                else t = -1;
            }
        }
        printf("%d %s\n" , ti, ac); 
    }
    return 0;
}