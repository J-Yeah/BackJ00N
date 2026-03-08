#include <stdio.h>
#include <math.h>

int main() {
    int m,n;
    scanf("%d %d", &m, &n);
    int arr[n+1];
    for (int i=0;i<=n;i++){
        arr[i] = i;
    }
    arr[1]=0;
    for (int i=2;i<=sqrt(n);i++){
        if (arr[i] == 0) continue;
        for (int j=i*2;j<=n;j+=i){
            arr[j] = 0;
        }
    }
    for (int i=m;i<=n;i++){
        if (arr[i]!=0){
            printf("%d\n", arr[i]);
        }
    }
    return 0;
}