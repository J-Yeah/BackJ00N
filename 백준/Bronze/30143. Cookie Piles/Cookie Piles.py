import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,a,d = map(int, input().split())
    print(n*(2*a + (n-1)*d)//2)