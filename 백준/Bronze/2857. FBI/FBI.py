total = list()

for i in range(5):
    a = input()
    try :
        a.index('FBI')
        total.append(i+1)
    except:
        pass

if len(total)==0 :
    print("HE GOT AWAY!")
else :
    for j in range(len(total)):
        print(total[j], end=' ')