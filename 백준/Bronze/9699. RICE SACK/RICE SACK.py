import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, n+1):
    a = list(map(int, input().split()))
    print(f"Case #{i}: {max(a)}")