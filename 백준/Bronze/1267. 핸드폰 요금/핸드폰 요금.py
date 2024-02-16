import sys

a = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
Y = 0
M = 0

for i in range(a):
    Y += num_list[i]//30 +1
    M += num_list[i]//60+1


Y *= 10
M *= 15

if Y<M :
    print("Y", Y)
elif M<Y :
    print("M", M)
else :
    print("Y M", Y)