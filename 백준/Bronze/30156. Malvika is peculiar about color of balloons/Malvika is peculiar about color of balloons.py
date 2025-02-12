import sys
for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip()
    print(min(a.count('a'), a.count('b')))