import sys
input = sys.stdin.readline
lst = list(int(input()) for _ in range(int(input())))
if len(lst)%2 == 1:
    print("still running")
else:
    result = 0
    for i in range(0, len(lst), 2):
        result += lst[i+1] - lst[i]
    print(result)