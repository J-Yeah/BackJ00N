import sys
input = sys.stdin.readline
n, m = map(int, input().split())

lst = list()
for _ in range(n):
    x = input().strip()
    lst.append(x)

def repaint_count(x, y):
    c1 = 0
    c2 = 0
    
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if lst[x + i][y + j] != 'W':
                    c1 += 1
                if lst[x + i][y + j] != 'B':
                    c2 += 1
            else: 
                if lst[x + i][y + j] != 'B':
                    c1 += 1
                if lst[x + i][y + j] != 'W':
                    c2 += 1
                    
    return min(c1, c2)

s = 50

for i in range(n - 7):
    for j in range(m - 7):
        s = min(s, repaint_count(i, j))

print(s)