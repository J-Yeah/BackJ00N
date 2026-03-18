#include <stdio.h>

int main() {
    int n, a, b, c, ans=0, cannot_cnt=0, m_cnt=0;
    scanf("%d", &n);
    int cnt[101] = {0,};
    for (int i=0;i<n;i++){
        scanf("%d %d %d", &a, &b, &c);
        cnt[a]++;
        cnt[b]++;
        cnt[c]++;
    }
    for (int i=100;i>0;i--){
        if (cnt[i]==0){
            int total = 99 - cannot_cnt - m_cnt;
            int k = 2 - m_cnt;
 
            if (k==0) ans += 1;
            else if (k==1) ans += total;
            else if (k==2) ans += total*(total-1)/2;
 
            cannot_cnt++;
        }
        else if (cnt[i]==1) m_cnt++;
    }
    printf("%d", ans);
    return 0;
}