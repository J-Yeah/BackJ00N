#include <stdio.h>
int main(void){
    int num;
    scanf("%d", &num);
    long arr[90] = {0, 1};
    for (int i=2;i<=num;i++)
        arr[i] = arr[i-1] + arr[i-2];
    printf("%ld", arr[num]);
    return 0;
}