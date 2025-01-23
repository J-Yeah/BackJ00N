#include <stdio.h>
int main(void){
	int t1,e1,f1,t2,e2,f2, total1, total2;
	scanf("%d %d %d\n%d %d %d", &t1,&e1,&f1,&t2,&e2,&f2);
	total1 = t1*3 + e1*20 + f1*120;
	total2 = t2*3 + e2*20 + f2*120;
	if (total1>total2) printf("Max");
	else if (total1<total2) printf("Mel");
	else printf("Draw");
	return 0;
}