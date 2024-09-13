score = list(map(int, input().split()))

cof = 0
hack = 0

for i in range(9) :
    if score[i] > (i+2)//2*100 :
        hack += 1

if hack > 0 :
    print("hacker")
elif sum(score) >= 100 :
    print("draw")
else :
    print("none")