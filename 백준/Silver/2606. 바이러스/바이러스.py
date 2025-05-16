import sys
input = sys.stdin.readline

def DFS(v):
    global cnt
    v_lst[v] = 1
    for j in lst[v]:
        if v_lst[j]==0:
            DFS(j)
            cnt += 1

n = int(input())
m = int(input())
lst = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

v_lst = [0]*(n+1)
v_lst[1] = 1
cnt = 0
DFS(1)
print(cnt)