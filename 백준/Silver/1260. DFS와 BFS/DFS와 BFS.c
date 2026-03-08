#include <stdio.h>
#include <string.h>
int graph[1001][1001] = {0, }, dfscheck[1001] = {0, }, queue[1001] = {0, }, bfscheck[1001] = {0, };

void dfs(int v, int n){ // 재귀함수로 구현
    dfscheck[v] = 1;
    printf("%d ", v);
    for (int i=0;i<=n;i++){
        if (graph[v][i]==1 && dfscheck[i]==0) dfs(i, n);
    }
}

void bfs(int v, int n){ // 큐로 구현
    int front=0, rear=0, pop, i;
    
    bfscheck[v] = 1;
    printf("%d ", v);
    queue[rear++] = v ;
    
    while (front<rear){
        pop = queue[front++];

        for (i = 1; i <= n; i++) {
            if (graph[pop][i] && bfscheck[i]==0) {
                printf("%d ", i);
                queue[rear] = i;
                rear++;
                bfscheck[i] = 1;
            }
        }
    }
}

int main() {
    int n,m,v,a,b;
    scanf("%d %d %d", &n, &m, &v);
    for (int i=0;i<m;i++){
        scanf("%d %d", &a, &b);
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
    
    dfs(v,n);
    printf("\n");
    bfs(v,n);
    
    return 0;
}