import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

cnt = {}
for card in a:
    cnt[card] = cnt.get(card, 0) + 1

for card in b:
    print(cnt.get(card, 0), end=' ')