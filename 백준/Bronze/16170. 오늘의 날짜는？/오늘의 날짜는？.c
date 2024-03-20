#include <stdio.h>
#include <time.h>

int main(void) {
	time_t timer = time(NULL);
	struct tm* t;
	t = localtime(&timer);

	printf("%d\n", t->tm_year+1900);
	printf("%d\n", t->tm_mon+1);
	printf("%d\n", t->tm_mday);

	return 0;
}