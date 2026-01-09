import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('#')
    elif n == 2:
        print('#'*2)
        print('#'*2)
    else:
        print('#'*n)
        for i in range(n-2):
            print('#'+'J'*(n-2)+'#')
        print('#'*n)
    print()