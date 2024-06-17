import sys

W, H, N = map(int, sys.stdin.readline().split())
num =0
X = []
Y = []
for i in range (N) :
    a, b = map(int, sys.stdin.readline().split())
    X.append(a)
    Y.append(b)

for i in range (N-1) :
    x, y = X[i]-X[i+1], Y[i]-Y[i+1]
    if x > 0 and y > 0 :
        num += max(abs(x), abs(y))
    elif x < 0 and y < 0 :
        num += max(abs(x), abs(y))
    else :
        num += abs(x)+abs(y)

print(num)