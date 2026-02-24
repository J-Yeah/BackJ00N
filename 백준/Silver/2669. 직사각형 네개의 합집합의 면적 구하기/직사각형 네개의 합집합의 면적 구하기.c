#include <stdio.h>

int main() {
    int adj[101][101], cnt=0;
	for (int i = 1; i <= 4; i++) {
		int a, b, c, d;
		scanf("%d %d %d %d", &a, &b, &c, &d);
		for (int y = b; y < d; y++) {
			for (int x = a; x < c; x++) {
				if (!adj[y][x]) {
					cnt++;
					adj[y][x] = 1;
				}
			}
		}
	}
	printf("%d", cnt);
    return 0;
}