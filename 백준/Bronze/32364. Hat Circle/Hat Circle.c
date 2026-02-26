#include <stdio.h>

int main() {
    int n, cnt=0;
    scanf("%d",&n);
    int h[n];
    for (int i=0;i<n;i++){
        scanf("%d", &h[i]);
    }
	for (int j=0;j<(n/2);j++){
	    if (h[j]==h[n/2+j]) cnt++;
	}
	printf("%d", cnt*2);
    return 0;
}