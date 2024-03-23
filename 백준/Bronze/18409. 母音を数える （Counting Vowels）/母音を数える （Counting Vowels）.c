#include <stdio.h>

int main(void){
	int leng, total=0;
	scanf("%d", &leng);
	char word[leng];
	scanf("%s", word);

	for (int i=0;i<leng;i++){
	if (word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'){
	total += 1;
}
}
	printf("%d", total);
	return 0;
}