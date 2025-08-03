n = [13,7,5,3,3,2]
col = list(map(int, input().split()))
enl = list(map(int, input().split()))
co = 0
en = 0
for i in range(6) :
    co += col[i]*n[i]
    en += enl[i]*n[i]
en += 1.5
if co>en :
    print("cocjr0208")
elif en>co :
    print("ekwoo")