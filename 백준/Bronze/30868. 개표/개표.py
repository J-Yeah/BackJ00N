import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print("++++ "*(n//5), end='')
    print("|"*(n%5))