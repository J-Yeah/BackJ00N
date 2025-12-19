import sys
input = sys.stdin.readline
pr = list()
for i in range(int(input())):
    a,b,c = map(int, input().split())
    pr.append([a,b,c,i+1])
pr.sort(key=lambda x:(-x[0], x[1], x[2]))
print(pr[0][3])