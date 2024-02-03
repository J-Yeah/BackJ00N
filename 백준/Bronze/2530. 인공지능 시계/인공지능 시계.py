time = list(map(int, input().split()))
sec = int(input())

time[2] += sec

if time[2] >= 60 :
    a = time[2]//60
    time[2] = time[2]%60
    time[1] += +a
if time[1] >= 60 :
    a = time[1]//60
    time[1] = time[1]%60
    time[0] += a
if time[0] >= 24 :
    time[0] = time[0]%24

for i in range(3) :
    print(time[i], end=' ')
