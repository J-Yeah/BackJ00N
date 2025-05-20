import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = list()
for _ in range(n):
    a.insert(0, int(input()))
coin = 0
for i in a:
    coin += k//i
    k = k%i
print(coin)