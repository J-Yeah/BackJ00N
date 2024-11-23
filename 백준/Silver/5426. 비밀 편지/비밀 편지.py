import sys
for _ in range(int(sys.stdin.readline())):
    s = list(sys.stdin.readline().strip())
    a = int(len(s)**0.5)
    w = ""
    for i in range(a):
        for j in range(a):
            w += s[j*a+(a-i-1)]
    print(w)