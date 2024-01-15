#include <stdio.h>

int main(void){
	char word, word_2;
	scanf("%c%c", &word, &word_2);

	float num = 0.0 ;

	switch (word) {
    	case 'A':
	    	num += 4;
		    break;
    	case 'B':
	    	num += 3;
		    break;
    	case 'C':
	    	num += 2;
		    break;
    	case 'D':
	    	num += 1;
		    break;
    	default:
	    	break;
	    }

	switch (word_2) {
	    case '+':
		    num += 0.3;
		    break;
	    case '-':
		    num -= 0.3;
    		break;
	    default:
    		break;
	    }

	printf("%.1f", num);
	return 0;
}