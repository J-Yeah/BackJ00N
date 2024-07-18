import sys
num = int(sys.stdin.readline())
tor = 0
for i in range(num):
    a = sys.stdin.readline()
    a = a.lower()
    try :
        a.index('pink')
        tor += 1
    except :
        try :
            a.index('rose')
            tor += 1
        except :
            pass
if tor == 0 :
    print("I must watch Star Wars with my daughter")
else :
    print(tor)