import sys

num = int(sys.stdin.readline())

for i in range(num) :
    a = int(sys.stdin.readline())
    dec = []
    while len(dec)< a*2 :
        dec.extend(map(int,sys.stdin.readline().split()))
    ts_total = 0
    da_total = 0
    for j in range(0,a*2,2) :
        if abs(dec[j]-dec[j+1])==1 :
            if (dec[j]==1 and dec[j+1]==2) :
                ts_total += 6
            elif (dec[j]==2 and dec[j+1]==1) :
                da_total += 6
            else :
                if dec[j]>dec[j+1] :
                    da_total += dec[j]+dec[j+1]
                elif dec[j]<dec[j+1] :
                    ts_total += dec[j]+dec[j+1]
        else :
            if dec[j]>dec[j+1] :
                ts_total += dec[j]
            elif dec[j]<dec[j+1] :
                da_total += dec[j+1]
    print(f"Game {i+1}: Tessa {ts_total} Danny {da_total}")