#include <stdio.h>

int main() {
    int t1,m1,s1,t2,m2,s2, t,m,s;
    scanf("%d:%d:%d", &t1, &m1, &s1);
    scanf("%d:%d:%d", &t2, &m2, &s2);
    t = t2-t1;
    m = m2-m1;
    s = s2-s1;
    if (t==0 && m==0 && s==0) {
        printf("24:00:00");
        return 0;
    }
    if (s<0) {
        m -= 1;
        s += 60;
    }
    if (m<0) {
        t -= 1;
        m += 60;
    }
    if (t<0) {
        t += 24;
    }
	if (t < 10) {printf("0");}
	printf("%d:", t);
    if (m < 10) {printf("0");}
	printf("%d:", m);
    if (s < 10) {printf("0");}
	printf("%d", s);
    return 0;
}