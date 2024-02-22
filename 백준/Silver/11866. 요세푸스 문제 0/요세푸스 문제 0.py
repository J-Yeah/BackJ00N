import sys

a,b = map(int, sys.stdin.readline().split())
num_list = list(range(1,a+1))
s = b-1

print("<", end='')

while len(num_list)>0 :
    s %= len(num_list)
    print(num_list.pop(s), end='')
    s += b-1
    if len(num_list)>0 :
        print(", ", end='')
print(">")