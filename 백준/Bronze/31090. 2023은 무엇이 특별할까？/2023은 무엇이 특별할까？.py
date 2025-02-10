import sys
for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if (a+1) % (a%100) == 0 :
        print("Good")
    else :
        print("Bye")