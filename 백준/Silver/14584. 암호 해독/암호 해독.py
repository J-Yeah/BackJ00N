import sys
input = sys.stdin.readline
text = input().strip()
a = list()
for i in range(int(input())):
    n = input().strip()
    a.append(n)
for j in range(1,27):
    pw = list()
    for char in text :
        nch = chr((ord(char) - ord('a') + j) % 26 + ord('a'))
        pw.append(nch)
    pw = ''.join(pw)
    for z in range(len(a)):
        if a[z] in pw :
            print(pw)
            break