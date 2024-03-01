import sys

num = int(sys.stdin.readline())

num_list = [0]*50
num_list[0] = 1

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    temp = num_list[a-1]
    num_list[a-1] = num_list[b-1]
    num_list[b-1] = temp

for i in range (50):
    if num_list[i-1]==1 :
        print (i)