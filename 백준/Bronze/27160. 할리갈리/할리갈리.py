import sys

num = int(sys.stdin.readline())
arr = [0,0,0,0]
for i in range (num) :
    a, b = sys.stdin.readline().split()
    if a=="STRAWBERRY" :
        arr[0] += int(b)
    elif a=="BANANA" :
        arr[1] += int(b)
    elif a=="LIME" :
        arr[2] += int(b)
    elif a=="PLUM" :
        arr[3] += int(b)

try:
    arr.index(5)
    print("YES")
except :
    print("NO")