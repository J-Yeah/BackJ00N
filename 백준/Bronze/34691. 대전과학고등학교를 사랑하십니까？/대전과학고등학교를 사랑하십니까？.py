import sys
input = sys.stdin.readline
while True :
    a = input().strip()
    if a == "animal" :
        print("Panthera tigris")
    elif a== "flower" :
        print("Forsythia koreana")
    elif a == "tree" :
        print("Pinus densiflora")
    elif a == "end" :
        break