#include <stdio.h>

int main() {
    int n, a, total= 0;
    scanf("%d", &n);
    if (n == 1) {
        printf("0");
        return 0;
    }
    int arr[n];
    scanf("%d", &a);
    for (int i=0;i<n-1;i++){
        scanf("%d", &arr[i]);
    }
    while (1) {
        int max_idx = 0;
        for (int j=1; j<n-1; j++) {
            if (arr[j] > arr[max_idx]) {
                max_idx = j;
            }
        }
        if (a<=arr[max_idx]){
            arr[max_idx]--;
            a++;
            total++;
        }
        else {
            printf("%d", total); 
            return 0;
        }
    }
}