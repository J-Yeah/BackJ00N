#include <stdio.h>
#include <math.h>

int main() {
    int w,h,n,a,b,paper;
    float letter;
    scanf("%d %d", &w, &h);
    scanf("%d %d %d", &n, &a, &b);
    letter = (w/a)*(h/b);
    paper = ceil(n/letter);
    if (paper>0){printf("%d", paper);}
    else {printf("-1");}
    return 0;
}