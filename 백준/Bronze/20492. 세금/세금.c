#include <stdio.h>

int main(void){
	int prize;
	scanf("%d", &prize);

	printf("%d %d", (int)(prize*0.78), (int)(prize*0.8+prize*0.2*0.78));
	return 0;
}
