import sys
rate, kwh = map(int, sys.stdin.readline().split())
for i in range(int(sys.stdin.readline())):
    us = int(sys.stdin.readline())
    if us <= 1000 :
        print(us, us*rate)
    else :
        print(us, 1000*rate+(us-1000)*kwh)