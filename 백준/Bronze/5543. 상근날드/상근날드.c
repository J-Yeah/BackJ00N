#include <stdio.h>
int main() {
	int b, d;
	int min = 0, min2 = 0;
	for (int i = 0; i < 3; i++) {
		scanf("%d", &b);
		if (min == 0 ) min = b;
		if (min > b) min = b;
		}
	for (int i = 0; i < 2; i++) {
		scanf("%d", &d);
		if (min2 == 0) min2 = d;
		if (min2 > d) min2 = d;
		}
	printf("%d", min + min2 - 50);
	return 0;
}