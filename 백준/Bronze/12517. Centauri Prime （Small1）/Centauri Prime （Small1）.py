import sys
t = int(sys.stdin.readline())
lst = list()
key = ['a', 'e', 'i', 'o', 'u']

for i in range(1, t+1):
    a = sys.stdin.readline().strip()
    if a[-1] == 'y' :
        y = "nobody"
    elif a[-1] in key :
        y = "a queen"
    else :
        y = "a king"
    print(f"Case #{i}: {a} is ruled by {y}.")