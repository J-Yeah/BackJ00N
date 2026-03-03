#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int n1 = *(int *)a;
    int n2 = *(int *)b;
    if (n1 < n2) return -1;
    if (n1 > n2) return 1;
    return 0;
}

int main() {
    int arr[4], b;
    for (int i=0;i<4;i++) scanf("%d", &arr[i]);
    scanf("%d", &b);
    
    qsort(arr, 4, sizeof(int), compare);
    
    if (arr[0]==arr[1] && arr[1]==arr[2] && arr[2]==arr[3]) printf("1");
    else if (arr[0]+b == arr[1] && arr[1]==arr[2] && arr[2]==arr[3]) printf("1");
    else printf("0");
    return 0;
}