#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int num1 = *(int *)a;
    int num2 = *(int *)b;
    if (num1 < num2) return -1;
    if (num1 > num2) return 1;
    return 0;
}

int main() {
    int n, total= 1, max_cnt = 1;
    scanf("%d", &n);
    if (n == 1) {
        printf("1");
        return 0;
    }
    int arr[n];
    for (int i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(arr[0]), compare);
    for(int i = 0 ; i < n ; i++) {
        if (arr[i] == arr[i-1]) {
            total++;
        } else {
            if (total > max_cnt) {max_cnt = total;}
            total = 1;
        }
    }
    if (total > max_cnt) {max_cnt = total;}
    printf("%d" , max_cnt); 
    return 0;
}