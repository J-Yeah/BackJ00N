import sys
input = sys.stdin.readline
x = list()
 
for _ in range(int(input())):
    a, b = map(int, input().split())
    x.append(a + b)
    
print(min(x))