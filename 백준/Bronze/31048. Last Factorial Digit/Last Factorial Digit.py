import sys
import math
input = sys.stdin.readline
for _ in range(int(input())):
    print(math.factorial(int(input()))%10)