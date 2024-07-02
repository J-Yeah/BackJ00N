a = int(input())
for i in range(a):
    lv, wv, le, we = map(int, input().split())
    if lv*wv > le * we: 
        print("TelecomParisTech")
    elif lv*wv < le*we :
        print("Eurecom")
    else : 
        print("Tie")