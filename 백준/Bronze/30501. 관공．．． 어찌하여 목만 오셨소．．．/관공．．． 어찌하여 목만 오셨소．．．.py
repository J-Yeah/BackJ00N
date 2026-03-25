import sys
x = list()
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip()
    x.append(a)
for i in range(len(x)):
    if 'S' in x[i] :
        print(x[i])
        break