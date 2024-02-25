import sys
num = int(sys.stdin.readline())

print("*"*num)

for i in range(1, num) :
    print(" "*(i-1), "*"*(num-i))